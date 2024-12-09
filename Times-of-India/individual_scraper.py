'''
Article synopsis - M1rHh
Article - _s30J '''

'''
#! This file scapes article pages not archive pages !!
'''

import requests
from bs4 import BeautifulSoup

class Main:
    def __init__(self, url: str):
        self.session = requests.Session()
        self.url = url
        # self.processing(self.session, self.url)

    def processing(self, session, url):
        response = session.get(url)       
        if response.status_code == 200:
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            
            try:
                self.article_summary = soup.find(class_='M1rHh').text
            except:
                self.article_summary = ""
            # for element in article_summary:
            #     print("Summary -", element.text)
            
            self.article = soup.find(class_='_s30J').text
            # for element in article:
            #     print("\nArticle -", element.text)
        else:
            print("Failed to retrieve the page. Status code:", response.status_code)
    
    def return_text(self):
        self.processing(self.session, self.url)
        return [self.article_summary, self.article]

if __name__ == "__main__":
    url = "http://timesofindia.indiatimes.com//india/follow-covid-protocol-as-cases-rising-in-many-nations-pm-modi/articleshow/96503095.cms"
    print(Main(url).return_text())
