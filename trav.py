#===================gridTraveler============================

def gridTraveler(m, n, memory={}):

    if (m,n) in memory:
        return memory[(m, n)]


    if ((m == 0) or (n == 0)):
        return 0
    elif (m == n == 1):
        return 1

    memory[(m, n)] = memory[(n, m)] = gridTraveler(m-1, n, memory) + gridTraveler(m, n-1, memory)

    return memory[(m, n)]


print(gridTraveler(3, 2))
print(gridTraveler(5, 6))
print(gridTraveler(18, 18))
#===================gridTraveler============================

