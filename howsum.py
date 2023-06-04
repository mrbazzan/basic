#===================howSum============================

# targetSum - number
# numbers - array of non-negative numbers
# returns an array containing any combination
# of elements that add up to exactly the targetSum.
# If there is no combination that adds up, the return
# None

def howSum(targetSum, numbers, memory={}):

    if targetSum == 0:
        return []

    for number in numbers:
        remainder = targetSum - number
        if remainder < 0:
            continue

        if remainder in memory:
            return memory[remainder]

        answer = howSum(remainder, numbers)
        memory[remainder] = answer

        if answer is not None:
            return answer + [number]

    return None

# print(howSum(8, [2, 3, 5]))
# print(howSum(7, [3, 5, 2]))
print(howSum(7, [2, 4]))
# print(howSum(0, [1, 2, 3]))
# print(howSum(7, [2, 4, 1]))
# print(howSum(7, [5, 3, 4, 7]))
# print(howSum(7, [2, 3]))
# print(howSum(7, [2, 3, 5]))
print(howSum(300, [7, 14]))
#===================howSum============================

