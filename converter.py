
""" Converts from fts to inches, yard, miles et.c"""

RATES = [12, 0.33, 0.000189, 304.8, 30.48, 0.3048, 0.0003048]


def converter(length, conversion):
    answer = length*RATES[conversion-1]
    return answer


the_length = float(input('Enter the length in feet: '))

print("""Choose:
        1- Convert to inches
        2- Convert to Yards
        3- Convert to miles
        4- Convert to millimeters
        5- Convert to centimeters
        6- Convert to metres
        7- Convert to kilometers""")


convert_to = int(input('Enter choice: '))

realAnswer = converter(the_length, convert_to)
print(realAnswer)
