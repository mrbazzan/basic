import requests
from bs4 import BeautifulSoup

def get_city_codes(url):
    # Error handling
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    # Parse content generated from the response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find data from the city section
    city_table = soup.find(
        "div", {"id": "collapseCityCodes"}
    ).find("table")

    # Extract the data
    header = city_table.find("thead")
    body = city_table.find("tbody").find_all("tr")

    header_data = [i.text.strip() for i in header.find_all("th")]
    body_data = [i.text.strip().split() for i in body]

    return header_data, body_data

if __name__ == "__main__":
    url = 'https://countrycode.org/afghanistan'
    header, body = get_city_codes(url)
    print(' '.join(header))
    print('\n'.join(' '.join(codes) for codes in body))

