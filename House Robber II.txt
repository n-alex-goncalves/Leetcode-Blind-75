class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        INPUT: list of integers
        OUTPUT: maximum money that can be robbed
        '''
        return max(nums[0] + self.linearRob(nums[2:-1]), self.linearRob(nums[1:]))
    
    def linearRob(self, nums: List[int]) -> int:
        num_len = len(nums)
        
        if num_len == 0: return 0
        if num_len == 1: return nums[0]
        if num_len == 2: return max(nums[0], nums[1])
        
        table = [-1 for i in range(num_len)]
        table[0] = nums[0]
        table[1] = max(nums[0], nums[1])
        
        for i in range(2, num_len):
            table[i] = max(table[i - 2] + nums[i], table[i - 1])
        
        return table[num_len - 1]