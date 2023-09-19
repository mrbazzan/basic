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

# Find data from the Statistics section
stat_tags = soup.find(
    'a', href="#collapseStatistics"
).find_next("div").find_all("ul")

info = []
for tag in stat_tags:
    data = tag.find("li").getText()
    if data.startswith(("Population", "Area", "GDP")):
        info.append(data)

for i in info:
    print(i.strip())

