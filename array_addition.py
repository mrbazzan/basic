# CODERBYTE: ARRAY ADDITION

# input = [1,1,2,3,4]
# output = true or false
#    combination of number (excluding the largest)
#    equal to the largest number



# find the max number, and seperate it out

def f(arr, large=None):
    if arr == []:
        return arr

    n = arr.pop()
    total = f(arr)

    num = [i + [n] for i in total]
    print("NUM: ", num)
    for data in num:
        if sum(data) == large:
            return 1

    total = total + [[n]] + num
    print("TOTAL: ", total)
    return total

def array_addition(arr):

    if f(sorted(arr)[:-1], large=max(arr)) == 1:
        return True
    return False

print(array_addition([5,7,16,1,2]))

