import requests
from bs4 import BeautifulSoup
import re
import url_generator
import individual_scraper

class Main:
    link_dict = {}

    def __init__(self):
        # Initialize the session
        self.s = requests.Session()

    def pre_processing(self, session, url):
        """
        Scrape the webpage to populate link_dict with article titles and URLs.
        """
        try:
            response = session.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                right_col_wrap_elements = soup.find_all(class_='rightColWrap')

                for element in right_col_wrap_elements:
                    a_tags = element.find_all('a')
                    for a in a_tags:
                        href = a.get('href')
                        if href:
                            # Handle relative and absolute URLs
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

    def search_articles(self, target_word):
        """
        Search for articles containing the target_word in their titles.
        """
        strings = self.link_dict.keys()
        matching_strings = [s for s in strings if re.search(rf'\b{target_word}\b', s, re.IGNORECASE)]

        print(f"{len(matching_strings)} article(s) found containing the word '{target_word}'.\n")
        for headline in matching_strings:
            print("Headline:", headline)
            print("Article Link:", self.link_dict[headline])
            # Example: Process each article with an external scraper
            individual_scraper.Main(self.link_dict[headline])
            print()

# Example usage
if __name__ == "__main__":
    target_date = "2024-11-15"
    target_word = "Modi"
    url = url_generator.Main(target_date).get_url()
    print("Generated URL:", url)

    main = Main()
    main.pre_processing(main.s, url)
    main.search_articles(target_word)