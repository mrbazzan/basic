#===================bestSum============================

# targetSum - number
# numbers - array of non-negative numbers
# returns an array containing the shortest combination
# of numbers that add up to exactly the targetSum

# If there is a tie, you may return any one of the
# shortest

def bestSum(targetSum, numbers, memory={}):
    if targetSum in memory:
        return memory[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    total = None
    for number in numbers:
        remainder = targetSum - number
        answer = bestSum(remainder, numbers, memory)

        if answer is not None:
            answer = [number] + answer

            if ((total is None) or len(answer) < len(total)):
                total = answer

    memory[targetSum] = total
    return total


print(bestSum(6, [2, 3, 5]))
# print(bestSum(8, [2, 3, 5]))
# print(bestSum(7, [3, 5, 2]))
# print(bestSum(7, [2, 4]))
# print(bestSum(0, [1, 2, 3]))
# print(bestSum(7, [2, 4, 1]))
# print(bestSum(7, [5, 3, 4, 7]))
# print(bestSum(7, [2, 3]))
# print(bestSum(7, [2, 3, 5]))
# print(bestSum(300, [7, 14]))
#===================bestSum============================

