'''
Article synopsis - M1rHh undefined
Article - _s30J clearfix  '''


import requests
from bs4 import BeautifulSoup

class Main:
    def __init__(self, url: str):
        # Start a session
        self.session = requests.Session()
        self.url = url
        self.processing(self.session, self.url)

    def processing(self, session, url):
        # Send a GET request to the URL
        response = session.get(url)
        
        # Check if request is successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find and print the article summary
            article_summary = soup.find_all(class_='M1rHh')
            for element in article_summary:
                print("Summary -", element.text)
            
            # Find and print the main article content
            article = soup.find_all(class_='_s30J')
            for element in article:
                print("Article -", element.text)
        else:
            print("Failed to retrieve the page. Status code:", response.status_code)

# Main execution
if __name__ == "__main__":
    url = ""
    Main(url)
