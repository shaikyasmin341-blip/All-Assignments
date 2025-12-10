""": Store API Results Locally
•	Instructions:
•	Extend your function from Task 4.
•	Save the extracted API results into a local file (results.json or results.txt).
•	Each new request should append results without overwriting old ones."""

import requests
import json
def get_weather(city):
    api_key = "29ddaea09248db24562c72fb891bf625"  # Your real API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        data = response.json()
        
        # Extract specific fields
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        
        # Prepare the result dictionary
        result = {
            "city": city,
            "temperature": temperature,
            "humidity": humidity,
            "description": description.capitalize()
        }
        
        # Display in user-friendly format
        print(f"Weather details for {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
        
        # Append results to a local file
        with open("results.json", "a") as file:
            file.write(json.dumps(result) + "\n")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # e.g. 404 Not Found
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")  # e.g. Network problem
    except KeyError as key_err:
        print(f"Key error occurred: {key_err}")  # e.g. Missing expected data
city_name = input("Enter a city name: ")
get_weather(city_name)

