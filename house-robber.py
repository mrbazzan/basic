
def rob(nums):
    highest = 0
    for i, num in enumerate(nums):
        if (i+2) < len(nums):
            nums[i+2] += nums[i]

        if nums[i] > highest:
            highest = nums[i]

    return highest


print(rob([1,2,3,1]))
print(rob([2,7,9,3,1]))

