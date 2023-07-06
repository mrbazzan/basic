#===================bestSum============================

# targetSum - number
# numbers - array of non-negative numbers
# returns an array containing the shortest combination
# of numbers that add up to exactly the targetSum

# If there is a tie, you may return any one of the
# shortest

def bestSum(targetSum, numbers):

    length = targetSum + 1
    arr = [None for _ in range(length)]
    arr[0] = []

    for i, state in enumerate(arr):
        for j in numbers:
            index = i+j
            if (arr[i] is not None) and (index < length):
                combination = arr[i] + [j]
                if arr[index] is None or (len(arr[index]) > len(combination)):
                    arr[index] = combination

    return arr[targetSum]

print(bestSum(6, [2, 3, 5]))
print(bestSum(8, [2, 3, 5]))
print(bestSum(7, [3, 5, 2]))
print(bestSum(7, [2, 4]))
print(bestSum(0, [1, 2, 3]))
print(bestSum(7, [2, 4, 1]))
print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(7, [2, 3]))
print(bestSum(7, [2, 3, 5]))
print(bestSum(300, [7, 14]))
#===================bestSum============================

