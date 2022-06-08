class Solution:
    def uniquePaths(self, m: int, n: int, memo = {}) -> int:
        '''
        INPUT: m columns, n rows
        OUTPUT: number of unique paths
        SOLUTION:
        
        tabulation
        
        2D table of size m n
        instantiated with 0, except 1 1 = 1
        
        for i j in 2D table
            starting from 1 1
            add value of current table above and to the left
            
        return 2D table position starting at m n
        
        '''
        
        table = [[0 for i in range(n + 1)] for j in range(m + 1)]
        table[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                table[i + 1][j] += table[i][j]
                table[i][j + 1] += table[i][j]
                
        return table[m - 1][n - 1]
        