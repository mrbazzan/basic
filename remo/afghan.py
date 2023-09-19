import requests
from bs4 import BeautifulSoup

url = 'https://countrycode.org/afghanistan'
# Error handling
try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)

# Parse content generated from the response
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the language tags in the Travel section
language_tags = soup.find(
    'a', href="#collapseTravel"
).find_next("div").find_all("ul")

# The fifth <ul> tag contains the languages
languages = language_tags[5].find("li").text.split(',')

# Extract the language names and percentage of speakers
for language in languages:
    print(language.strip())

