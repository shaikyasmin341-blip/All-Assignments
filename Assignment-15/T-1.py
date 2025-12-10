#write a python function that display weather details of a city using weather api without error handling. Display weather details as JSON output

import requests
import json

def get_weather(city):
    api_key = "370e6f154e75be9fa82c021e7a54dc71"  # Your real API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()
    print(json.dumps(data, indent=4))

city_name = input("Enter a city name: ")
get_weather(city_name)

