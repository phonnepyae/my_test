import json
import requests

url ='https://api.openweathermap.org/data/2.5/weather?appid=ab927d7076cae28312326f9a3a9d060f&q='

user_input = input("Please enter your city name  ")

new_url = url+user_input

data = requests.get(new_url).json()

# Print both keys and values using zip
print("Keys and Values:")
for key, value in zip(data.keys(), data.values()):
	print(f"{key}: {value}")

print(type(data))