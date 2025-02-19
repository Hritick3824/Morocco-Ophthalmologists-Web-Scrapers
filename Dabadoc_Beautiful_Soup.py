import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_name(soup):
    try:
        return soup.find('h1').text.strip()
    except AttributeError:
        return ""

def get_occupation(soup):
    try:
        return soup.find('h2').text.strip()
    except AttributeError:
        return ""

def get_address(soup):
    try:
        return soup.find('div', attrs={"class": "card-text"}).text.strip()
    except AttributeError:
        return ""

def fetch_and_parse_url(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        print("Failed to retrieve the webpage. Status code:", response.status_code)
        return None

def get_website(soup):
    link_tag = soup.find('a', class_='profile-website-link')
    return link_tag['href'].strip() if link_tag and 'href' in link_tag.attrs else ""

def get_phone_number(soup):
    phone_tag = soup.find('a', {'id': 'phone-number-btn'})
    return phone_tag['href'].split(':')[1].strip() if phone_tag and 'href' in phone_tag.attrs and 'tel' in phone_tag['href'] else ""

def get_care(soup):
    elements = soup.find_all('a', class_="badge badge-secondary p-2 mb-1")
    return ', '.join(element.text.strip() for element in elements)

def get_diplomas_and_training(soup):
    doctor_entries = soup.find_all('div', class_='card')
    diplomas_and_training = []
    for entry in doctor_entries:
        card_title_element = entry.find('h3', class_='card-title')
        card_title = card_title_element.get_text(strip=True) if card_title_element else 'No title available'
        if card_title == 'Education':
            list_items = entry.find_all('li')
            diplomas_and_training = [item.get_text(strip=True) for item in list_items]
    return ' ; '.join(diplomas_and_training)

def get_languages_spoken(soup):
    doctor_entries = soup.find_all('div', class_='card')
    for entry in doctor_entries:
        card_title_element = entry.find('h3', class_='card-title')
        card_title = card_title_element.get_text(strip=True) if card_title_element else 'No title available'
        if card_title == 'Languages Spoken':
            return entry.find('div', class_='card-text').text.strip()
    return ""

def scrape_page(url, headers):
    soup = fetch_and_parse_url(url, headers)
    links = [a.get('href') for a in soup.find_all('a', class_='profile_url')] if soup else []
    return links

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    }
    base_url = 'https://www.dabadoc.com/search?button=&country=MA&search%5Bbooking_type%5D=0&search%5Bcity_id%5D=&search%5Bdoctor_speciality_id%5D=51d6e1f4ef96750d4d000027&search%5Btype%5D=false&page={}'
    page = 1
    data = []

    while True:
        url = base_url.format(page)
        print(f"Scraping page {page}: {url}")
        links = scrape_page(url, headers)

        if not links:
            break

        for link in links:
            res = requests.get(link, headers=headers)
            if res.status_code == 200:
                doc_soup = BeautifulSoup(res.text, 'html.parser')
                data.append({
                    'Name': get_name(doc_soup),
                    'Occupation': get_occupation(doc_soup),
                    'Address': get_address(doc_soup),
                    'Phone_Number': get_phone_number(doc_soup),
                    'Website': get_website(doc_soup),
                    'Care': get_care(doc_soup),
                    'Diplomas_and_Training': get_diplomas_and_training(doc_soup),
                    'Languages_Spoken': get_languages_spoken(doc_soup),
                    'Profile_Link': link
                })

        page += 1

    df = pd.DataFrame(data)
    df['Occupation'] = df['Occupation'].str.replace('\n', ' ', regex=False)
    df['Address'] = df['Address'].str.replace('\n', ' ', regex=False)
    df.replace('\n', ' ', regex=True, inplace=True)
    df.to_excel('dabadoc_ophthalmologist.xlsx', index=False)
