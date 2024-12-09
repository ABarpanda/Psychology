import json
from bs4 import BeautifulSoup
from datetime import datetime, date, timedelta
import timeit
import Times_of_India as toi
import csv

epoch = date(1900, 1, 1)
start_date = date.fromisoformat("2022-01-01")
end_date = date.fromisoformat("2022-12-31")
"""
end_date > start_date
"""

target_words = ["PM Modi"]

date_links = {}
start_date_int = (start_date - epoch).days
end_date_int = (end_date - epoch).days

# print(toi.Main(start_date,target_word).search_articles())

start = timeit.default_timer()

for day in range(start_date_int,end_date_int+1):
    date_links[(epoch + timedelta(days=day)).strftime("%Y-%m-%d")] = toi.Main(epoch + timedelta(days=day),target_words).search_articles()
    data = f"\"{(epoch + timedelta(days=day)).strftime("%Y-%m-%d")}\" : {date_links[(epoch + timedelta(days=day)).strftime("%Y-%m-%d")]}"
    with open("Modi_links.json", "a") as file:
        file.write(data+",\n")


print(json.dumps(date_links,indent=4))

end = timeit.default_timer()

print("Total time taken -", end-start)