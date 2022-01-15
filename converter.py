
""" Converts from fts to inches, yard, miles et.c"""

# TODO: Set up PYTHON OOP PROJECTS FOLDER
# TODO: DO a .gif for the scripts

RATES = [12, 0.33, 0.000189, 304.8, 30.48, 0.3048, 0.0003048]

units = {
    1: 'inches', 2: 'yards', 3: 'miles', 4: 'millimeters', 5: 'centimeters', 6: 'metres', 7: 'kilometers',
}


def converter(length, conversion):
    answer = length * RATES[conversion - 1]
    return answer


the_length = float(input('Enter the length in feet: '))

print("""Choose:
        1- Convert to Inches
        2- Convert to Yards
        3- Convert to Miles
        4- Convert to Millimeters
        5- Convert to Centimeters
        6- Convert to Metres
        7- Convert to Kilometers""")

convert_to = int(input('Enter choice: '))
while convert_to not in units.keys():
    convert_to = int(input('Enter choice: '))

realAnswer = converter(the_length, convert_to)

print('\n\t' + str(realAnswer) + ' ' + units[convert_to])
