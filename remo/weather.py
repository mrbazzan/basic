import sys
import requests

# Define the API URL and parameters
API_KEY= "" # Replace this with key generated from openweathermap.org
location = "Nigeria"

url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"

# Make a GET request to the API
response = requests.get(url)

# Check if the request was not successful (status code 200)
if response.status_code != 200:
    print("Failed to retrieve weather data.")
    sys.exit()

# Parse the JSON response
weather_data = response.json()

# Extract the temperature
temperature_kelvin = weather_data['main']['temp']
temperature_fahrenheit = (temperature_kelvin - 273.15) * 9/5 + 32
temperature_celsius = temperature_kelvin - 273.15

# Print the temperature in Celsius
print(f"Temperature in {location}: {temperature_celsius:.2f}°C")

