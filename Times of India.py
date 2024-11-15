import requests
from bs4 import BeautifulSoup
import re
import url_generator
import indivisual_scraper

# Define the date variable as needed (format it based on your requirements)
date = "2014-11-15"

# Generate URL using url_generator
url = url_generator.Main(date).get_url()
print("Generated URL:", url)

# Define the data structures
link_dict = {}

# Start a session
s = requests.Session()

def pre_processing(session, url):
    # Send a GET request to the URL
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

# Call the function
pre_processing(s, url)

# print(link_dict)
# print(link_dict.keys())


# List of strings
strings = link_dict.keys()

# Word to search for
word = "Modi"

# Find strings containing the whole word
matching_strings = [s for s in strings if re.search(rf'\b{word}\b', s)]
# print(matching_strings)

for headline in matching_strings:
    print("Link Text:", headline)
    print("Headline:", link_dict[headline])
    indivisual_scraper.Main(link_dict[headline])
    print()