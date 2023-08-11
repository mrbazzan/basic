import sys

def feet_converter(fts: float, rate: float) -> float:
    """
    Convert a length in feet to another unit.

    Args:
        fts (float): The length in feet.
        rate (float): The conversion rate for the unit.

    Returns:
        float: The converted length.
    """
    return fts * rate

units = {
    1: 'inches',
    2: 'yards',
    3: 'miles',
    4: 'millimeters',
    5: 'centimeters',
    6: 'metres',
    7: 'kilometers',
}

try:
    length = float(input('Enter the length in feet: '))
except ValueError:
    print("Enter a valid length")
    sys.exit(1)

print("""Choose:
        1- Convert to Inches
        2- Convert to Yards
        3- Convert to Miles
        4- Convert to Millimeters
        5- Convert to Centimeters
        6- Convert to Metres
        7- Convert to Kilometers
        (Any Other Number) - Enter Custom Rate""")

RATES = [12, (1/3), 0.000189, 304.8, 30.48, 0.3048, 0.0003048]
si_unit = ''

try:
    unit = int(input('Enter choice: '))
except ValueError:
    print("Enter a valid unit")
    sys.exit(1)

if unit not in range(8):
    try:
        rate = float(input('Enter custom rate: '))
    except ValueError:
        print("Enter a valid rate")
        sys.exit(1)
else:
    rate = RATES[unit - 1]
    si_unit = units[unit]

answer = feet_converter(length, rate)
print('\n\t' + str(answer) + ' ' + si_unit)
