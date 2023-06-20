class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        INPUT: list of integers
        OUTPUT: maximum money that can be robbed without alterting police
        SOLUTION:
        memo index
        '''
        num_len = len(nums)
        if (num_len == 1): return nums[0]
        if (num_len == 2): return max(nums[0], nums[1])
        memo = [-1 for i in range(num_len)]
        return self.helper(nums, num_len - 1, memo)
        
    def helper(self, nums: List[int], index, memo) -> int:
        if (memo[index] != -1): return memo[index]
        if (index < 0): return 0
        
        memo[index] = max(nums[0] + self.helper(nums[2:], index - 2, memo), self.helper(nums[1:], index - 1, memo))
        return memo[index]
        