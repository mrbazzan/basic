import csv

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
    # Call the function to extract data for each country
    extract_data('Moldova')
    extract_data('Norway')

