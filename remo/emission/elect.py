import csv
import argparse

def extract_data(country):
    with open('electricity.csv', 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

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
        choices=[
            'Mexico', 'Moldova', 'Netherlands',
            'New Zealand', 'Nigeria', 'Norway',
            'Pakistan', 'Portugal'],
        help='Country for which to extract data'
    )
    args = parser.parse_args()

    extract_data(args.country)
