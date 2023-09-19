import csv

def calculate_average(data):

    # Get the index of 2008
    year = data[0].index('2008')
    

    # Extract the electricity per capita for 2008
    # from the data
    year_data = [float(row[year]) for row in data[1:]]

    # Return the average electricity per capita for 2008
    return sum(year_data) / len(year_data)

# Load data from the csv file 
with open('electricity.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# Calculate the average electricity per capita for 2008
average_electricity_per_capita = calculate_average(data)

print('Average electricity per capita for 2008 is:', average_electricity_per_capita)
