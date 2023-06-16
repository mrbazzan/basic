#===================howSum============================

# targetSum - number
# numbers - array of non-negative numbers
# returns an array containing any combination
# of elements that add up to exactly the targetSum.
# If there is no combination that adds up, the return
# None

def howSum(targetSum, numbers):

    length = targetSum + 1
    arr = [None for _ in range(length)]
    arr[0] = []

    for i, state in enumerate(arr):
        for j in numbers:
            index = i+j
            if (arr[i] is not None) and (index < length):
                arr[index] = arr[i] + [j]

    return arr[targetSum]

# print(howSum(8, [2, 3, 5]))
# print(howSum(7, [5, 3, 4]))
# print(howSum(7, [2, 4]))
# print(howSum(0, [1, 2, 3]))
print(howSum(7, [2, 4, 1]))
# print(howSum(7, [5, 3, 4, 7]))
# print(howSum(7, [2, 3]))
# print(howSum(7, [2, 3, 5]))
# print(howSum(300, [7, 14]))
#===================howSum============================
