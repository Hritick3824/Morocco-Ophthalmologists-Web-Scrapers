import requests
from bs4 import BeautifulSoup
import pandas as pd

# Send a GET request to the URL

from googletrans import Translator
language = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
googletrans_translator = Translator()
def language_translation(input_string,source_lan,target_lag):
    global googletrans_translator,language
    
    try : 
        googletrans_result = googletrans_translator.translate(input_string,src= "auto", dest= language[target_lag])
        googletrans_result = googletrans_result.text
    except : 
        googletrans_result = input_string
    return googletrans_result


def get_data(link):
    
    response = requests.get(link)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    doctor_div1 = soup.find_all('div', class_='cn-list-row cn-list-item vcard individual')
    doctor_div2 = soup.find_all('div', class_="cn-list-row-alternate cn-list-item vcard individual")
    doctor_div = doctor_div1 + doctor_div2 
    all_data = []
    for doctor in doctor_div:
        doctor_info = {}
        try:
            link = doctor.find('a')['href']
            group_name = doctor.find('span',class_='given-name').text.strip()
            family_name = doctor.find('span',class_='family-name').text.strip()
            specialty = doctor.find('span',class_='title notranslate').text.strip()
            sector = doctor.find('span',class_='organization-name notranslate').text.strip()
            address = language_translation(doctor.find('span',class_ = 'street-address notranslate' ).text.strip(),'','english')
            
            doctor_info['name'] = group_name + ' ' + family_name
            doctor_info['specialty'] = specialty
            doctor_info['sector'] = sector
            doctor_info['address'] = address
            doctor_info['link'] =  link
            all_data.append(doctor_info)
        except:
            pass
    
    return all_data
    



doctor_list_all = []
for i in range(1,572):
    url = "https://www.cromc.ma/recherche/pg/" + str(i) + "/?cn-s&cn-cat=0"
    data = get_data(url)
    print("page " + str(i) + " done ==> length -->" , len(data))
    doctor_list_all.extend(data)
    
    

df = pd.DataFrame(doctor_list_all,columns=['name','specialty','sector','address','link'])
df.to_excel('cromc_data_new_final.xlsx',index=False)