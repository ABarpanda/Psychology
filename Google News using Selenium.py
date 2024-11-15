from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options for headless browsing (if needed)
options = Options()
options.add_argument("--headless")  # Runs Chrome in headless mode.
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open Google News
url = 'https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en'
driver.get(url)

# Optional: Scroll down the page to load more articles
scrolls = 5  # Number of times to scroll down
for _ in range(scrolls):
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(1)  # Wait for articles to load

# Find all articles
articles = driver.find_elements(By.TAG_NAME, 'article')
newslist = []

# Extract titles and links from articles
for item in articles:
    try:
        # Find the title and link
        title_element = item.find_element(By.TAG_NAME, 'h3')
        title = title_element.text
        link_element = title_element.find_element(By.TAG_NAME, 'a')
        link = link_element.get_attribute('href')
        
        # Append to newslist
        newslist.append({'title': title, 'link': link})
    except Exception as e:
        print(f"Error parsing an article: {e}")
        continue

# Close the WebDriver
driver.quit()

# Print results
print(f"Found {len(newslist)} articles:")
for article in newslist:
    print(article)
