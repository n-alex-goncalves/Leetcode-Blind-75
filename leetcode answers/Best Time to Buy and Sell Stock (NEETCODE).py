class Solution(object):
    def maxProfit(self, prices):
        """
        INPUT: prices
        OUTPUT: maximum profit that can made
        SOLUTION:
        
        
        left, right = 0, 0
        
        
        right += 1
        
        if right < left:
            left = right
            
        left, right is index
        
        
        
        left, right = 0, 1
        maximum_output, len_prices = 0, len(prices)
        
        while right < len_prices:
            if prices[left] < prices[right]:
                left = right
            else:
                maximum_output = max(maximum_output, prices[right] - prices[left])
            right += 1
        
        return maximum_output
        """
        left, right = 0, 1
        maximum_output, len_prices = 0, len(prices)
        
        while right < len_prices:
            if prices[left] > prices[right]:
                left = right
            else:
                maximum_output = max(maximum_output, prices[right] - prices[left])
            right += 1
        
        return maximum_output