import requests

url = "https://india-today-unofficial.p.rapidapi.com/news/Sports"

headers = {
	"x-rapidapi-key": "6e21947f9fmshee9ad4e3e587570p17e864jsn0958834a65e2",
	"x-rapidapi-host": "india-today-unofficial.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response)