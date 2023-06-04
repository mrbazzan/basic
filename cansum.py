#===================canSum============================

# targetSum - number
# numbers - array of non-negative numbers
# returns a boolean indicating whether or not
# it is possible to generate the targetSum
# using numbers from the array.
def canSum(targetSum, numbers, memory={}):

    if targetSum == 0:
        return True

    # if targetSum < 0:
    #     return False

    for number in numbers:
        if number > targetSum:
            continue

        if targetSum in memory:
            return memory[targetSum]

        if canSum(targetSum-number, numbers, memory):
            memory[targetSum] = True
            return True


    memory[targetSum] = False
    return False

# print(canSum(7, [8, 5, 6]))
# print(canSum(7, [2, 4]))
# print(canSum(7, [2, 4, 1]))
# print(canSum(7, [5, 3, 4, 7]))
# print(canSum(7, [2, 3]))
# print(canSum(7, [2, 3, 5]))
print(canSum(300, [7, 14]))
#===================canSum============================

