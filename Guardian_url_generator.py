import requests
import dotenv
import os
import Guardian_search
from bs4 import BeautifulSoup

dotenv.load_dotenv()
guardian_api_key = os.getenv("guardian_api_key")
BASE_URL = "https://content.guardianapis.com"

def fetch_articles(query, page=1, page_size=10):
    if not guardian_api_key:
        return {"error": "Guardian API key is not configured."}

    url = f"{BASE_URL}/search"
    params = {
        "q": query,
        "api-key": guardian_api_key,
        "page": page,
        "page-size": page_size,
        "from-date": "2014-01-01",
        "to-date": "2024-12-01"
    }

    try:
        response = requests.get(url, params=params)
        print(response.url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

if __name__ == "__main__":
    search_query = "PM Modi AND Peace"
    print(f"Searching for articles about: {search_query}")
    
    result = fetch_articles(search_query) #* result is a json type
    if "response" in result and "results" in result["response"]:
        for article in result["response"]["results"]:
            print(f"- {article['webTitle']} ({article['webUrl']})")
            
        print(result)
    else:
        print(result)
    # Guardian_search.