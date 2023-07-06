
def countNegative(grid):

    column = len(grid[0]) - 1
    row = total = 0

    while column >= 0 and row < len(grid):

        print(row, column)
        if grid[row][column] < 0:
            total = total + (len(grid) - row)
            column = column - 1

        if grid[row][column] >= 0:  # NB: elif is faster
            row = row + 1

    return total


print(countNegative(
[
    [4,3,2,-1],
    [3,2,1,-1],
    [1,1,-1,-2],
    [-1,-1,-2,-3]
]))

print(countNegative(
[
    [-1,-2,-3,-4],
    [-2,-3,-4,-5],
    [-3,-4,-5,-6],
    [-4,-5,-6,-7]
]))

print(countNegative([[5,1,0],[-5,-5,-5]]))

print(countNegative(
[
    [3,2],
    [1,0]
]))

