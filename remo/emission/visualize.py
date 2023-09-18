import csv
import matplotlib.pyplot as plt

def main():
    # load the data into a dictionary
    # where key is the country, and
    # value is each year's data for that country
    data = {}
    with open('data.csv') as file:
        f = csv.reader(file)
        for row in f:
            data.setdefault(row[0], row[1:])

    country = 'Chad'
    years = data['CO2 per capita']

    plt.figure(figsize=(10, 6))
    plt.plot(years, list(map(lambda x: float(x), data[country])), label=f'{country}')

    # set the labels for the plot
    plt.xlabel('Year')
    plt.ylabel(f'CO2 Level for {country}')
    plt.title('Year vs CO2 Level for Chad')
    plt.legend()

    # plot the graph
    plt.show()

if __name__ == "__main__":
    main()

