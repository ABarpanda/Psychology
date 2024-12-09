import requests
from bs4 import BeautifulSoup
import re
import url_generator
import individual_scraper
from datetime import datetime, date, timedelta
from typing import List

#todo: Try to ensure that "article(s) found containing the word" is not printed in link_matrix

class Main:
    def __init__(self, target_date:date, target_words:List[str]):
        self.s = requests.Session()
        self.target_date = target_date
        self.target_words = target_words

        url = url_generator.Main(target_date).get_url()
        self.url = url
        self.link_dict = {}

    def pre_processing(self):
        try:
            response = self.s.get(self.url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                right_col_wrap_elements = soup.find_all(class_='rightColWrap')

                for element in right_col_wrap_elements:
                    a_tags = element.find_all('a')
                    for a in a_tags:
                        href = a.get('href')
                        if href[:4] != "http":
                            href = "https://timesofindia.indiatimes.com/" + href
                        self.link_dict[a.text.strip()] = href
            else:
                print(f"Failed to retrieve the page. Status code: {response.status_code}")
        except Exception as e:
            print("Error during page retrieval:", str(e))
            print(
                "Please check your internet connection and try the following steps:\n"
                "   - Check the network cables, modem, and router\n"
                "   - Reconnect to Wi-Fi\n"
                "   - Run Windows Network Diagnostics"
            )

    def search_articles(self):
        Main.pre_processing(self)
        strings = self.link_dict.keys()
        matching_strings = [s for s in strings if all(re.search(rf'\b{word}\b', s, re.IGNORECASE) for word in self.target_words)]

        print(f"{len(matching_strings)} article(s) found on {self.target_date}.\n")

        links = []
        for headline in matching_strings:
            print("Headline:", headline)
            print("Article Link:", self.link_dict[headline])
            individual_scraper.Main(self.link_dict[headline])
            links.append(self.link_dict[headline])
            print()
        return links

if __name__ == "__main__":
    target_date = "2015-06-21"
    target_words = ["PM Modi", "education"]

    main = Main(target_date,target_words)
    main.pre_processing()
    article_links = main.search_articles()