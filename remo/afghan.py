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

# Find data from the URLs section
urls_tag = soup.find(
    'a', href="#collapseURLs"
).find_next("div").find("ul")

# Extract the urls 
urls = urls_tag.text.strip().split('\n')
for url in urls:
    print("https://www." + url)

