class Solution:
    def climbStairs(self, n: int, memo = {}) -> int:
        table = [0 for i in range(n + 2)]
        table[0] = table[1] = 1
        
        for i in range(n):
            table[i + 2] += table[i]
            table[i + 1] += table[i]
        
        return table[n - 1]