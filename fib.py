

#===================fibonacci============================
def fib(n):
    if n <= 2:  return 1
    return fib(n-1) + fib(n-2)


# print(fib(6))
# print(fib(7))
# print(fib(50))


# memoization

def fibonacci(n, memory={1:1, 2:1}):
    if n in memory: return memory[n]
    memory[n] = fibonacci(n-1, memory) + fibonacci(n-2, memory)

    return memory[n]



print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(50))


#===================fibonacci============================

