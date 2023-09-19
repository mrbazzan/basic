import csv
import argparse

def electricity_data():
    with open('electricity.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    return data

def get_country_list():
    # NB: The first row of the data contains the header,
    # so there is a need to skip it
    countries = [row[0] for row in electricity_data()[1:]]
    return countries

def extract_data(country):
    data = electricity_data()

    with open(f'{country}.csv', 'w', newline='') as f:
        writer = csv.writer(f)

        # Write the header
        writer.writerow(data[0])

        # Write the data for the specified country
        for row in data:
            if row[0] == country:
                writer.writerow(row)

    print(f'Data successfully extracted for {country}, and saved into {country}.csv')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Extract electricity data for a given country'
    )
    parser.add_argument(
        '--country',
        required=True,
        choices=get_country_list(),
        help='Country for which to extract data'
    )

    # Get the option from the user
    args = parser.parse_args()
    extract_data(args.country)

