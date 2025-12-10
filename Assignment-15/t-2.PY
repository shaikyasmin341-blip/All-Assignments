#Prompt: write a python function that display weather details of a city using weather api with error handling. Display weather details as JSON output

import requests
import json
def get_weather(city):
    api_key = "29ddaea09248db24562c72fb891bf625"  # Your real API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}" 
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        data = response.json()
        print(json.dumps(data, indent=4))
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # e.g. 404 Not Found
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")  # e.g. Network problem
    except json.JSONDecodeError as json_err:
        print(f"JSON decode error occurred: {json_err}")  # e.g. Invalid JSON
city_name = input("Enter a city name: ")
get_weather(city_name)

