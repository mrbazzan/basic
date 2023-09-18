import csv 

# load data from the csv file 
with open('electricity.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

with open('nigeria.csv', 'w', newline='') as nigeria:
    writer = csv.writer(nigeria)

    # Write the header
    writer.writerow(data[0])

    # Write the data for Nigeria by iterating over the `data`
    for row in data:
        if row[0] == 'Nigeria':
            writer.writerow(row)

print('Data successfully extracted for Nigeria, and saved into nigeria.csv')

