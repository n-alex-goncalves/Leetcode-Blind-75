class Solution:
    def fib(self, n: int) -> int:
        '''
        INPUT: n index
        OUTPUT: corresponding number
        
        SOLUTION: 
        
        tabulation
        create a table of size n
        instantiate with 0
        instantiate index 1 with 1
        
        add index to next two positions
        return table[n]
        
        '''
        
        table = [0 for i in range(n + 2)]
        table[1] = 1
        
        for i in range(n):
            table[i + 1] += table[i]
            table[i + 2] += table[i]
        
        return table[n]