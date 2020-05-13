
""" Converts from fts to inches, yard, miles et.c"""


def converter():
    print("""Choose:
       1- Convert to inches
       2- Convert to Yards
       3- Convert to miles
       4- Convert to millimeters
       5- Convert to centimeters
       6- Convert to metres
       7- Convert to kilometers""")

    rates = [12, 0.33, 0.000189, 304.8, 30.48, 0.3048, 0.0003048]

    length = int(input('Enter the length in feet: '))
    conversion = int(input('Enter choice: '))

    answer = length * rates[conversion - 1]
    return answer


realAnswer = converter()
print(realAnswer)
