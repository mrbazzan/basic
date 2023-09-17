import csv 

# load the data into a dictionary
with open('data.csv') as file: 
    data = list(csv.reader(file)) 

# Get the index of the year
i = data[0].index('2000') 

# Initialize min, max values and corresponding countries 
min_val, max_val = float('inf'), float('-inf') 
max_countries, min_countries = [], []

# Iterate over the data 
for row in data[1:]:
    val = float(row[i])

    # Get minimum data
    if val < min_val:
        min_val = val 
        min_countries = [row[0]] 
    elif val == min_val:
        min_countries.append(row[0])

    # Get maximum data
    if val > max_val:
        max_val = val 
        max_countries = [row[0]] 
    elif val == max_val:
        max_countries.append(row[0])

print(f'\nIn 2000, countries with minimum and maximum CO2 emission '
      f'levels were: {min_countries} and {max_countries} respectively.')
