import requests
from bs4 import BeautifulSoup
from datetime import date
import re
import url_generator
import individual_scraper

target_date = "2013-01-01"

url = url_generator.Main(target_date).get_url()
print("Generated URL:", url)


# Define the data structures
link_dict = {}

# Start a session
s = requests.Session()

def pre_processing(session, url):
    # Send a GET request to the URL
    try:
        response = session.get(url)
        # response = s.get(url)
        
        # Check if request is successful
        if response.status_code == 200:
        # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find elements with class 'rightColWrap'
            right_col_wrap_elements = soup.find_all(class_='rightColWrap')
            
            # Print each element found (or access specific content within it)
            for element in right_col_wrap_elements:
                # Find all <a> tags within the current 'rightColWrap' element
                a_tags = element.find_all('a')
                
                # Print each <a> tag and its href attribute (if it exists)
                for a in a_tags:
                    # print("Link Text:", a.text)
                    # print("Link URL:", a.get('href'))
                    link_dict[a.text] = a.get('href')
        else:
            print("Failed to retrieve the page. Status code:", response.status_code)
    except:
        print("Failed to retrieve the page. Please check your internet connection")
        print("No internet \n   Try: \n       Checking the network cables, modem, and router\n       Reconnecting to Wi-Fi\n       Running Windows Network Diagnostics")

# Call the function
pre_processing(s, url)
