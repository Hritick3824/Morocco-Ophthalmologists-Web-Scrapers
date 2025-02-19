# import requests
# from bs4 import BeautifulSoup

# # Send a GET request to the URL

# from googletrans import Translator
# language = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
# googletrans_translator = Translator()
# def language_translation(input_string,source_lan,target_lag):
#     global googletrans_translator,language
#     print(input_string)
#     googletrans_result = googletrans_translator.translate(input_string,src= "auto", dest= language[target_lag])
#     return googletrans_result.text

# def get_address(link):
#     doctor_info = {}
#     response = requests.get(link)
#     response.raise_for_status()
#     soup = BeautifulSoup(response.text, 'html.parser')
#     doctor_name = soup.find('div', class_='content is-flex is-flex-direction-column')
#     name = doctor_name.find('h1').text.strip()
#     specialty = doctor_name.find('h2').text.strip()
#     city = doctor_name.find('h3').text.strip()
#     doctor_info['name'] = name
#     doctor_info['specialty'] = specialty
#     doctor_info['city'] = city
#     doctor_entries = soup.find_all('div', class_='card profile-card mb-5')
    
#     for entry in doctor_entries:
        
#         try:
#             value = entry.find('h3',class_='').text.strip()
#             address = entry.find('p' , class_='has-text-weight-bold text-slate-900').text.strip()
#             doctor_info[value] = address
#         except:
#             address = ''
    
#     return doctor_info
    

# all_doctors_list = []

# for i in range(1,2):

#     response = requests.get('https://www.doctolist.com/en/morocco/doctors/ophthalmologist?page=' + str(i))
#     response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

#     # Parse the content with BeautifulSoup
#     soup = BeautifulSoup(response.text, 'html.parser')

#     doctor_entries = soup.find_all('div', class_='column is-2-tablet-only is-4-desktop')

#     # Extract information for each doctor
#     doctors = []
#     for entry in doctor_entries:
#         doctor_info = {}
#         link = entry.find('a')['href']
        
#         get_address_list = get_address(link)

#         img = entry.find('img')['src']
#         name = entry.find('h2', class_='std-card-data-item').text.strip()
#         specialty = entry.find('h3', class_='std-card-data-item').text.strip()
#         location = entry.find('h4', class_='std-card-data-item').text.strip()

#         doctor_info['name'] = get_address_list['name']
#         doctor_info['specialty'] = get_address_list['specialty']
#         doctor_info['city'] = get_address_list['city']
#         doctor_info['address'] = get_address_list['Address']
#         doctor_info['link'] = link
#         doctor_info['spoken_languages'] = get_address_list['Spoken languages']
#         doctor_info['means_of_payment'] = get_address_list['Means of payment']
#         doctor_info['img'] = img

#         doctors.append(doctor_info)

#     all_doctors_list.extend(doctors)
#     print(f'Page {i} of 10 scraped')
    
# import pandas as pd
# df = pd.DataFrame(data= all_doctors_list,columns = ['name','specialty','city','address','link','spoken_languages','means_of_payment','img'])
# df.to_csv('doctors_list_doctolist_new.csv', index=False)



""" 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

# Initialize Selenium webdriver (you may need to specify the path to your webdriver)
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--lang=en")
chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors
chrome_options.add_argument("--allow-running-insecure-content") 

# Use WebDriverManager to automatically manage ChromeDriver
webdriver_service = Service(ChromeDriverManager().install())

# Initialize the Chrome driver
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

import pandas as pd

df = pd.read_csv("doctors_list_doctolist_new.csv")

phone_number_list = []

for i in range(len(df)):
    
    val = df.iloc[i]
    link = val['link']
    
    driver.get(link)

    try : 
        # Find and click the "Show number" button
        show_number_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Show number')]")))
        show_number_button.click()

        # Wait for the phone number to be displayed
        phone_number_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[starts-with(text(), '+')]")))

        # Extract the phone number from the element
        phone_number = phone_number_element.text.strip()
        
    except:
        phone_number = ''

    # Print the extracted phone number
    phone_number_list.append(phone_number)
    
    print(str(i + 0))
    
# Close the webdriver
driver.quit()

df['phone_number'] = phone_number_list

df['phone_number'] = df['phone_number'].astype(str).str.replace('.0', '')

df.to_excel("doctors_list_doctolist_new_phone.xlsx", index=False)

"""





import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

language = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
googletrans_translator = Translator()
def language_translation(input_string,source_lan,target_lag):
    global googletrans_translator,language
    print(input_string)
    googletrans_result = googletrans_translator.translate(input_string,src= "auto", dest= language[target_lag])
    return googletrans_result.text

def get_address(link):
    doctor_info = {}
    response = requests.get(link)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    doctor_name = soup.find('div', class_='content is-flex is-flex-direction-column')
    name = doctor_name.find('h1').text.strip()
    specialty = doctor_name.find('h2').text.strip()
    city = doctor_name.find('h3').text.strip()
    doctor_info['name'] = name
    doctor_info['specialty'] = specialty
    doctor_info['city'] = city
    doctor_entries = soup.find_all('div', class_='card profile-card mb-5')
    
    for entry in doctor_entries:
        try:
            value = entry.find('h3',class_='').text.strip()
            address = entry.find('p' , class_='has-text-weight-bold text-slate-900').text.strip()
            doctor_info[value] = address
        except:
            address = ''
    
    return doctor_info

all_doctors_list = []

for i in range(1,11):
    response = requests.get('https://www.doctolist.com/en/morocco/doctors/ophthalmologist?page=' + str(i))
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    doctor_entries = soup.find_all('div', class_='column is-2-tablet-only is-4-desktop')
    doctors = []
    
    for entry in doctor_entries:
        doctor_info = {}
        link = entry.find('a')['href']
        get_address_list = get_address(link)
        img = entry.find('img')['src']
        doctor_info['name'] = get_address_list['name']
        doctor_info['specialty'] = get_address_list['specialty']
        doctor_info['city'] = get_address_list['city']
        doctor_info['address'] = get_address_list.get('Address', '')
        doctor_info['link'] = link
        doctor_info['spoken_languages'] = get_address_list.get('Spoken languages', '')
        doctor_info['means_of_payment'] = get_address_list.get('Means of payment', '')
        doctor_info['img'] = img
        doctors.append(doctor_info)
    
    all_doctors_list.extend(doctors)
    print(f'Page {i} scraped')
    
df = pd.DataFrame(data= all_doctors_list, columns=['name','specialty','city','address','link','spoken_languages','means_of_payment','img'])
df.to_csv('doctors_list_doctolist_new.csv', index=False)

chrome_options = Options()
# chrome_options.add_argument("--headless")
webdriver_service = Service('chromedriver\chromedriver.exe')
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

phone_number_list = []
for i in range(len(df)):
    val = df.iloc[i]
    link = val['link']
    driver.get(link)
    try:
        show_number_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Show number')]")))
        show_number_button.click()
        phone_number_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[starts-with(text(), '+')]")))
        phone_number = phone_number_element.text.strip()
    except:
        phone_number = ''
    phone_number_list.append(phone_number)
    print(str(i))

driver.quit()
df['phone_number'] = phone_number_list
df['phone_number'] = df['phone_number'].astype(str).str.replace('.0', '')
df.to_excel("doctors_list_doctolist_new_phone.xlsx", index=False)



'''---------------------------- FOR TRANSLATION----------------------------'''
# import pandas as pd

# # Read the Excel file
# df = pd.read_excel("Doctolist_ophthalmologist.xlsx")

# # Assuming the source language is English ('en') and target language is specified (e.g., 'spanish')
# source_language = ''
# target_language = 'english'

# # Apply the translation function to the 'address' column
# df['address'] = df['address'].apply(lambda x: language_translation(x, source_language, target_language))

# # Save the translated addresses back to the Excel file or another file
# df.to_excel("Translated_DoctorList_ophthalmologist.xlsx", index=False)