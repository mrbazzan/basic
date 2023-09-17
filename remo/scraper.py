import csv
import requests
import matplotlib.pyplot as plt

from bs4 import BeautifulSoup

def scrape_data(url):
    # Error handling
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    # Parse content generated from the response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Store country information
    countries = []

    # Returns all the rows of the scraped table
    table = soup.find('table').findAll('tr')
    for table_data in table:
        country_info = []

        # For each row, iterate over its columns
        for i, td in enumerate(table_data.findAll('td')):
            # Remove ISO codes from each country's data
            if i == 2:
                continue

            # Get required data from the column
            if td.find('a'):
                country_info.append(td.find('a').text.title())
            else:
                country_info.append(td.text)

        if country_info:
            countries.append(country_info)

    return countries

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Country Name', 'Country Code', 'Population', 'Area', 'GDP'])
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    url = "https://countrycode.org"
    data = scrape_data(url)

    save_to_csv(data, "countries.csv")
    print("File saved to countries.csv")
