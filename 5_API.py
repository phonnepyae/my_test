import json
import requests

my_key = "ab927d7076cae28312326f9a3a9d060f"

url ="http://api.openweathermap.org/data/2.5/weather?q=Mandalay&appid=ab927d7076cae28312326f9a3a9d060f"

j_data = requests.get(url).json()

print(j_data)