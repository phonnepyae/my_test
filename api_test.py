import requests

url = "http://api.openweathermap.org/data/2.5/weather?q=Mandalay&appid=ab927d7076cae28312326f9a3a9d060f"

try:
    print("Sending request...")
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    print("Request successful!")
    print(response.json())
except requests.exceptions.Timeout:
    print("The request timed out. Check your internet connection.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
