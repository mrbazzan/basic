#===================gridTraveler============================

def gridTraveler(m, n):

    arr = []
    for _ in range(m+1):
        array = []
        for _ in range(n+1):
            array.append(0)
        arr.append(array)
    arr[1][1] = 1

    for i, grid in enumerate(arr):
        for j in range(len(grid)):

            if (j+1) < len(grid):
                arr[i][j+1] = arr[i][j+1] + arr[i][j]

            if (i+1) < len(arr):
                arr[i+1][j] = arr[i+1][j] + arr[i][j]

    return arr[i][j]


# print(gridTraveler(3, 3))
print(gridTraveler(3, 2))
# print(gridTraveler(5, 6))
# print(gridTraveler(18, 18))
#===================gridTraveler============================

