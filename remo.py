

def median_price(prices):
    # find the number of the prices
    length = len(prices)

    # sort the prices in ascending order
    sorted_price = sorted(prices)

    # find the quotient (whole number gotten from the result of division)
    mid = length // 2

    # check if the length is odd or even.
    # if it is odd, the median is the middle value
    # if it is even, the median is the average of the middle
    # value and the number before the middle value
    if length % 2 != 0:
        return sorted_price[mid]
    else:
        return (sorted_price[mid-1] + sorted_price[mid])/2

# Driver code
stock_prices = [100, 110, 120, 105, 115]
print("The median price is: " + str(median_price(stock_prices)))

