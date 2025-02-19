import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def init_driver():
    service = Service(executable_path=driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=fr")
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def get_info(url, driver):
    try:
        # Load the webpage
        driver.get(url)

        # Click on the "Afficher le Téléphone" button to reveal the phone number
        phone_button = driver.find_element(By.ID, 'telephoneFirme')
        phone_button.click()

        # Wait until the phone number is displayed
        phone_element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, 'telephoneFirmeDisplay'))
        )

        # Extract the name
        name_element = driver.find_element(By.CLASS_NAME, 'nomprenomclient')
        name = name_element.text

        # Extract the address
        address_element = driver.find_element(By.CLASS_NAME, 'adresseclient')
        address = address_element.text

        # Extract the phone number
        phone = phone_element.text

        return name, address, phone, url
    except Exception as e:
        logging.error(f"Error retrieving info from {url}: {e}")
        return None, None, None, url

def scrape_profile_urls(driver, url):
    driver.get(url)

    # Find all the doctor links within the 'nomprenomclient' class
    doctor_links = driver.find_elements(By.CSS_SELECTOR, '.nomprenomclient a')

    # Extract href attribute from each link and construct the profile page URL
    profile_pages = []
    for link in doctor_links:
        href = link.get_attribute('href')
        if href and not href.startswith("mailto:"):
            # Correct duplicated domain part in URL
            href = href.replace('https://www.medicalis.mahttps://www.medicalis.ma', 'https://www.medicalis.ma')
            profile_pages.append(href)

    return profile_pages

def worker(url):
    driver = init_driver()
    result = get_info(url, driver)
    driver.quit()
    return result

# Specify the path to the ChromeDriver executable if it's not in PATH
driver_path = "chromedriver\chromedriver.exe"  # Replace with your path to chromedriver

# URL of the page to scrape
url = 'https://medicalis.ma/liste?tags=Ophtalmologue+&ReferenceVille=054'

# Create and open the CSV file for writing with French encoding
csv_file_path = "Marrakech.csv"
with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Address', 'Phone', 'Profile URL'])

    # Initialize the Chrome driver for URL scraping
    driver = init_driver()

    # Refresh the page multiple times and scrape new doctor profiles each time
    for _ in tqdm(range(40)):
        profile_pages = scrape_profile_urls(driver, url)

        # Use ThreadPoolExecutor to scrape profile pages concurrently
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(worker, profile_url) for profile_url in profile_pages]
            
            for future in as_completed(futures):
                name, address, phone, profile_url = future.result()
                if name and address and phone:
                    writer.writerow([name, address, phone, profile_url])
                else:
                    writer.writerow(['Unable to retrieve information', '', '', profile_url])

        # Wait for a while before refreshing the page again (to avoid spamming the server)
        time.sleep(3)

    # Clean up the URL scraping driver
    driver.quit()
