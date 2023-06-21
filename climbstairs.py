
class Solution:

    def climbStairs(self, n: int, memory={}) -> int:
        if n in memory:
            return memory[n]

        if n == 0:
            return 1
        
        if n < 0:
            return 0
        
        total = 0

        result = self.climbStairs(n-1, memory) + self.climbStairs(n-2, memory)
        if result:
            total += result

        memory[n] = total
        return total

    def climbStairs_tab(self, n: int) -> int:

        arr = [0 for _ in range(n+1)]
        arr[0] = 1

        for i, state in enumerate(arr):
            if i < n:
                arr[i+1] += arr[i]
            if i < n-1:
                arr[i+2] += arr[i]        

        return arr[n]


print(Solution().climbStairs(50))
print(Solution().climbStairs_tab(50))

