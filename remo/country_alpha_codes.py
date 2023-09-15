import csv
import requests
from bs4 import BeautifulSoup

def get_country_codes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    ans = soup.find('table', {'id': 'myTable'})

    country_data = []
    for code in ans.find_next('tbody').find_all("tr"):
        country_name, alpha2, alpha3, _ = code.text.strip().split("\n")
        country_data.append([country_name, alpha2, alpha3])

    return country_data

if __name__ == "__main__":
    url = "https://www.iban.com/country-codes"
    country_lists = get_country_codes(url)

    filename = "country.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["country-name", "alpha2-code", "alpha3-code"])
        writer.writerows(country_lists)

    print(f"Data successfully saved to {filename}")


    from pathlib import Path

    # Check if the country folder exists
    p = Path('~/country').expanduser()
    if not p.exists():
        p.mkdir()

    # Move to the country folder
    Path(filename).rename(Path(p, filename))
    print("File moved successfully.")

    # Get the size of the folder
    print(f"The size of the folder is: {Path(p, filename).stat().st_size}")

