
def findOdd(series):
    # Write your code here
    
    result = {}
    for element in series:
        diff = []
        for i in range(1, len(element)):
            diff.append(ord(element[i]) - ord(element[i-1]))

        if tuple(diff) in result:
            result[tuple(diff)] = 0
        else:
            result[tuple(diff)] = element

    for value in result.values():
        if value:
            return value

print(findOdd(["AC", "BD", "CE", "DE"]))
print(findOdd(["ACB", "BDC", "CED", "DEF"]))
 
