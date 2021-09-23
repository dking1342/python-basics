import requests

city = input("enter a title: ").upper()
base_url = "http://api.plos.org/search?q=title:" + city
print(base_url)
weather_data = requests.get(base_url).json()
print(weather_data)