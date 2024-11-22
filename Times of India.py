import requests
from bs4 import BeautifulSoup
import re
import url_generator
import individual_scraper

target_date = "2024-11-15"
target_word = "Modi"

url = url_generator.Main(target_date).get_url()
print("Generated URL:", url)

link_dict = {}

s = requests.Session()

def pre_processing(session, url):    
    try:
        response = session.get(url)        
                
        if response.status_code == 200:        
            soup = BeautifulSoup(response.text, 'html.parser')
                        
            right_col_wrap_elements = soup.find_all(class_='rightColWrap')
                        
            for element in right_col_wrap_elements:                
                a_tags = element.find_all('a')
                                
                for a in a_tags:
                    # print("Link Text:", a.text)
                    # print("Link URL:", a.get('href'))
                    if a.get('href')[:4]!="http":
                        link_dict[a.text] = "https://timesofindia.indiatimes.com/" + a.get('href')
                    else:
                        link_dict[a.text] = a.get('href')
        else:
            print("Failed to retrieve the page. Status code:", response.status_code)
    except:
        print("Failed to retrieve the page. Please check your internet connection")
        print("No internet \n   Try: \n       Checking the network cables, modem, and router\n       Reconnecting to Wi-Fi\n       Running Windows Network Diagnostics")


pre_processing(s, url)

# print(link_dict)
# print(link_dict.keys())

strings = link_dict.keys()
# print(link_dict)

matching_strings = [s for s in strings if re.search(rf'\b{target_word}\b', s)]
print(f"{len(matching_strings)} article(s) found")

for headline in matching_strings:
    print("Headline:", headline)
    print("Article Link:", link_dict[headline])
    individual_scraper.Main(link_dict[headline])
    print()