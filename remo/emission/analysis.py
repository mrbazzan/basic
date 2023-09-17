import csv 

def get_average(data, year):
    # Get the index of the year
    i = data[0].index(year)

    # calculate the sum of CO2 levels
    sum_val = 0

    # iterate over the data in other to calculate
    # the total sum of CO2 level for 2001
    for row in data[1:]:
        val = float(row[i])
        sum_val += val

    # calculate average
    average = sum_val / len(data[1:])
    return average

def main():
    # load the data into a dictionary
    with open('data.csv') as file: 
        data = list(csv.reader(file)) 

    average_2000 = get_average(data, '2000')
    average_2002 = get_average(data, '2002')

    print(f'\nIn 2000, the average CO2 level was {average_2000}.')
    print(f'\nIn 2002, the average CO2 level was {average_2002}.')

if __name__ == "__main__":
    main()
