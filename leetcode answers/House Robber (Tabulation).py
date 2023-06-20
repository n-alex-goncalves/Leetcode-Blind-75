class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        INPUT: list of integers nums
        OUTPUT: maximum houses that can be robbed
        SOLUTION:
        in dynamic programming questions, there's always a choice that can be made
        in this case, the choice is whether to rob or not to rob the current house
        '''
        num_length = len(nums)
        
        if num_length == 1: return nums[0]
        if num_length == 2: return max(nums[0], nums[1]) 
        
        table = [0 for i in range(num_length)]
        
        table[0] = nums[0]
        table[1] = max(nums[0], nums[1])
        
        for i in range(2, num_length):
            table[i] = max(table[i - 1], table[i - 2] + nums[i])
        
        return table[-1]