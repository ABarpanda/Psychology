import json
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
import re
import url_generator
import individual_scraper
import Times_of_India as toi

epoch = date(1900, 1, 1)
start_date = date.fromisoformat("2013-01-01")
end_date = date.fromisoformat("2013-01-31")
"""
end_date > start_date
"""

target_word = "Modi"

date_links = {}
start_date_int = (start_date - epoch).days
end_date_int = (end_date - epoch).days

print(toi.Main(start_date,target_word).search_articles())

for day in range(start_date_int,end_date_int+1,5):
    date_links[(epoch + timedelta(days=day)).strftime("%d-%m-%Y")] = toi.Main(epoch + timedelta(days=day),target_word).search_articles()

print(json.dumps(date_links,indent=4))