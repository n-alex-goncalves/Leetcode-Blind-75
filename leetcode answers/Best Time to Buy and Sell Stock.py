class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        INPUT: list of integers representing prices
        OUTPUT: maximum profit possible
        SOLUTION:
        
        left, right
        
        move left to right if right is less than left
        if right < left:
            left = right
        
        increment by right every time
        
        keep maximum 
        
        '''
        
        left, right, output, length = 0, 1, 0, len(prices)
        
        while right < length:
            if prices[right] < prices[left]:
                left = right
            else:
                output = max(output, prices[right] - prices[left])
            right += 1
        
        return output