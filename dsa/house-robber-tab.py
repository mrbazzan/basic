
def rob(nums):
    arr = [0 for _ in range(len(nums))]
    arr[0] = nums[0]

    for i in range(1, len(nums)):
        two_step = arr[i-2] if i >= 2 else 0
        arr[i] = max(nums[i] + two_step, arr[i-1])

    return arr[-1]


print(rob([1,2,2,4,1]))
print(rob([1,2,2,2,1]))
print("---------: ", rob([1,2,3,1]))
print("---------: ", rob([2,1,1,2]))
print("---------: ", rob([1,2,7,8,4,5]))
print("---------: ", rob([2,7,9,3,1]))

print(rob([
    183,219,57,193,94,233,202,154,
    65,240,97,234,100,249,186,66,
    90,238,168,128,177,235,50,81,
    185,165,217,207,88,80,112,78,
    135,62,228,247,211
]))

