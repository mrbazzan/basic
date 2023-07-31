
import matplotlib.pyplot as plt

# values for x-axis
d = ["2023-07-01", "2023-07-02", "2023-07-03", "2023-07-04", "2023-07-05"]

# values for y-axis
stock_prices = [100, 110, 120, 105, 115]

# plot the data
plt.plot(
    d,
    stock_prices,
    marker="o",
    linestyle="-",
    color="b",
    label="Stock Price"
)

# set the name of x and y axis
plt.xlabel("Date")
plt.ylabel("Price")

plt.grid(True)
plt.legend()

# fit plot within figure cleanly.
plt.tight_layout()

# display the line plot
plt.show()

