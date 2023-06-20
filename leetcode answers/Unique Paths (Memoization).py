class Solution:
    def uniquePaths(self, m: int, n: int, memo = {}) -> int:
        '''
        INPUT: m column and n rows
        OUTPUT: number of unique possible paths
        SOLUTION:
        
        memoization
        dictionary
        key | item
        
        if m < 0 or n < 0:
            return 0
        
        if ('m|n' in memo): return memo['m|n']
        if ('1|1'): return 1
        
        memo['m|n'] = uniquePaths(m - 1, n) + uniquePaths(m, n - 1)
        return memo['m|n']
        
        '''
        
        if m < 0 or n < 0:
            return 0
        
        key = str(m) + '|' + str(n)
        if (key in memo): return memo[key]
        if (key == '1|1'): return 1
        
        memo[key] = self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        return memo[key]