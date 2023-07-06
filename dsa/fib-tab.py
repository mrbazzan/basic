

#===================fibonacci============================
# tabulation

def fibonacci(n):
    arr = [0 for i in range(n+1)]
    arr[1] = 1

    i = 0
    while (i < n):
        arr[i+1] = arr[i+1] + arr[i]
        if i < n-1:
            arr[i+2] = arr[i+2] + arr[i]
        i+=1

    # for i in range(len(arr)-1):
    #     arr[i+1] = arr[i+1] + arr[i]
    #     if i < n-1:
    #         arr[i+2] = arr[i+2] + arr[i]

    return arr[n]


print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(50))


#===================fibonacci============================

