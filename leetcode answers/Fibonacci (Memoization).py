class Solution:
    def fib(self, n: int, memo = {}) -> int:
        '''
        INPUT: n - index of the fibonacci sequence
        OUTPUT: corresponding number
        
        fib(0) = 0
        fib(1) = 1
        fib(2) = 1
        fib(3) = 2
        ...
        
        SOLUTION:
        
        memoization - remember the answers for the previous calls.
        dictionary[2] = fib(2)
        fib(100) = fib(99) + fib(98)
        
        is it in the dictionary
        is it a base case
        
        calculuate
        return
        '''
        if (n in memo): return memo[n]
        if (n == 0): return 0
        if (n == 1): return 1
        
        memo[n] = self.fib(n - 1) + self.fib(n - 2)
        return memo[n]