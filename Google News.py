from requests_html import HTMLSession
from requests_html import HTML

# Initialize session
session = HTMLSession()

# Get the page
try:
    r = session.get('https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en')
except Exception as e:
    print("Failed to retrieve the page:", e)
    exit()

# Render the HTML
try:
    r.html.render(sleep=1, scrolldown=5)
except Exception as e:
    print("Error during rendering:", e)
    exit()

# Find all articles and initialize a list for storing news items
articles = r.html.find('article')
newslist = []

# Loop through each article to get title and link
for item in articles:
    try:
        newsitem = item.find('h3', first=True)  # Finds the main headline in <h3> tag
        title = newsitem.text if newsitem else "No title found"
        link = list(newsitem.absolute_links)[0] if newsitem else "No link found"  # Converts set to list
        newsarticle = {
            'title': title,
            'link': link 
        }
        newslist.append(newsarticle)
    except Exception as e:
        print(f"Error parsing an article: {e}")
        continue  # Skip to the next article in case of error

# Print the length and items of the list
print(f"Found {len(newslist)} articles:")
for article in newslist:
    print(article)
