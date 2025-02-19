import requests
from bs4 import BeautifulSoup

# Send a GET request to the URL

from googletrans import Translator
language = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
googletrans_translator = Translator()
def language_translation(input_string,source_lan,target_lag):
    global googletrans_translator,language
    googletrans_result = googletrans_translator.translate(input_string,src= "auto", dest= language[target_lag])
    return googletrans_result.text


def get_address(link):
    
    response = requests.get(link)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    doctor_div = soup.find_all('div', class_='strip_list wow fadeIn')
    all_data = []
    for doctor in doctor_div:
        doctor_info = {}
        try:
            link = doctor.find('a')['href']

            specialty = doctor.find('small').text.strip()
            name = doctor.find('h3').text.strip()
            address = language_translation(doctor.find('p').text.strip(),'','english')
            phone  = doctor.find_all('a')[-1].text.strip().split(':')[-1]

            doctor_info['name'] = name
            doctor_info['specialty'] = specialty
            doctor_info['address'] = address
            doctor_info['link'] = "https://www.marocmedecin.com" + link
            doctor_info['phone'] = phone
            
            all_data.append(doctor_info)
        except:
            pass
    
    return all_data
    
    

doctor_list_all = []
for i in range(19):
    url = "https://www.marocmedecin.com/medecin/rechercher-un-medecin.htm/page:" + str(i + 1) + "?data%5BDoctor%5D%5Bspecialties%5D=5&data%5BDoctor%5D%5Bcity_id%5D=&data%5BDoctor%5D%5Bnom%5D=&data%5BDoctor%5D%5Bprenom%5D=&data%5BDoctor%5D%5Bcodepostal%5D="
    data = get_address(url)
    doctor_list_all.extend(data)
    print("page",i+1,"scraped")
    
import pandas as pd
df = pd.DataFrame(doctor_list_all,columns=['name','specialty','address','link','phone'])
df.to_excel('marocmedecin_data_new.xlsx',index=False)

