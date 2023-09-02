import matplotlib.pyplot as plt
import pathlib
from datetime import datetime

# Set the directory path
directory = pathlib.Path("~", "Desktop", "lineplot").expanduser()

# Create the directory if it doesn't exist
directory.mkdir(parents=True, exist_ok=True)

# values for x-axis 
date = list(map(lambda x: datetime.strptime(x, "%Y-%m-%d"), ["2023-08-07", "2023-08-08", "2023-08-09", "2023-08-10", "2023-08-11", "2023-08-15", "2023-08-20", "2023-08-24"]))

rates = [751.12, 750.97, 769.27, 769.24, 769.20, 760, 746, 755.71]

plt.figure(figsize=(10, 6))

# Generate the line plot
plt.plot(
    date,
    rates,
    marker="o",
    linestyle="-",
    color="r",

)

# Set the name of x and y axis
plt.ylabel('Dollar to Naira Price')
plt.xlabel('Date')
plt.grid(True)

plt.title('Dollar-to-Naira Exchange Rate Line Plot')

# Save the image
saved_file = directory / "line.png"
plt.savefig(saved_file)

# Get the size of the saved file
size = saved_file.stat().st_size

print(f"The size of the saved file is: {size/1024/1024} MB")

plt.show()
