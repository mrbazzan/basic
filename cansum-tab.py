#===================canSum============================

# targetSum - number
# numbers - array of non-negative numbers
# returns a boolean indicating whether or not
# it is possible to generate the targetSum
# using numbers from the array.
def canSum(targetSum, numbers):

    length = targetSum + 1
    arr = [False for _ in range(length)]
    arr[0] = True

    for i, state in enumerate(arr):
        for j in numbers:
            index = i+j
            if state and (index < length):
                arr[index] = state

    # for i, state in enumerate(arr):
    #     if state:
    #         for j in numbers:
    #             index = i+j
    #             if index < length:
    #                 arr[index] = state



    return arr[targetSum]


print(canSum(7, [5, 3, 4]))
print(canSum(7, [2, 4, 1]))
print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 3]))
print(canSum(7, [2, 3, 5]))
print(canSum(7, [2, 4]))
print(canSum(300, [7, 14]))
#===================canSum============================

