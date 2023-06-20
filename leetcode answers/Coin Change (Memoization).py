import numpy as np

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        INPUT: integer array coins, integer amount
        OUTPUT: fewest number of coins that you need to make up the amount
        SOLUTION:
        
        what is the recurrence relation?
        
        coins = [1, 2, 3]
        
        the choice is any one of the coins
        
        until we reach zero,
        
        then we return min
        
        return the number of coins
        
        so...
        
        can't think of a solution with tabulation, so recursion it is    
        '''
        memo = dict()
        output = self.helper(coins, amount, memo)
        return output if output != np.inf else -1 
        
    def helper(self, coins: List[int], amount: int, memo) -> int:
        if (amount in memo): return memo[amount]
        if (amount == 0): return 0
        if (amount < 0): return np.inf
        
        memo[amount] = min([self.helper(coins, amount - coin, memo) for coin in coins]) + 1
        return memo[amount]