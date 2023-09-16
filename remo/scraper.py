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

def create_scatter_plot(data):
    plt.figure(figsize=(20, 6))

    countries_with_a  = [c for c in data if c[0].lower().startswith('a')]
    countries, population = [], []
    for country in countries_with_a:
        c = country[0]
        # convert comma seperated digit to float. e.g
        # 12,345 -> 12345.0
        population = float(''.join(country[3].split(',')))
        plt.scatter(c, population)

    plt.xlabel('Country Code')
    plt.ylabel('Population(1e7)')
    plt.title('Population Scatter Plot of Countries Starting with "A"')

    return plt

def create_line_plot(data):
    plt.figure(figsize=(20, 6))

    countries_starting_with_d = [c for c in data if c[0].lower().startswith('d')]
    c, gdp = [], []
    for country in countries_starting_with_d:
        c.append(country[0])

        # convert gdb to float. e.g
        # 18.56 Billion -> 18.56
        gdp.append(float(country[4].split(' ')[0]))

    plt.plot(c, gdp)

    plt.xlabel('Country Code')
    plt.ylabel('GDP(1e9)')
    plt.title('GDP Line Plot of Countries Starting with "D"')

    return plt

if __name__ == "__main__":
    url = "https://countrycode.org"
    data = scrape_data(url)
    plt = create_line_plot(data)
    print("Use `.show()` on `plt` to display the figure")
    plt.show()
