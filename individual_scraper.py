'''
Article synopsis - M1rHh undefined
Article - _s30J clearfix  '''

'''
#! This file scapes article pages not archive pages !!
'''

import requests
from bs4 import BeautifulSoup

class Main:
    def __init__(self, url: str):
        self.session = requests.Session()
        self.url = url
        self.processing(self.session, self.url)

    def processing(self, session, url):
        response = session.get(url)       
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            article_summary = soup.find_all(class_='M1rHh')
            for element in article_summary:
                print("Summary -", element.text)
            
            article = soup.find_all(class_='_s30J')
            for element in article:
                print("\nArticle -", element.text)
        else:
            print("Failed to retrieve the page. Status code:", response.status_code)

if __name__ == "__main__":
    url = "https://timesofindia.indiatimes.com//life-style/health-fitness/diet/7-healthy-mood-lifters/articleshow/27750314.cms"
    Main(url)
