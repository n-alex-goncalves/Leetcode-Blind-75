class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = dict()
        num_len = len(nums)
        if (num_len == 1): return True
        return self.helper(nums, num_len - 1, memo)
        
    def helper(self, nums: List[int], jump, memo) -> bool:
        if (jump in memo): return memo[jump]
        if (jump == 0): return True
        if (jump < 0): return False
        
        memo[jump] = any([self.helper(nums[i:], jump - i, memo) for i in range(1, nums[0] + 1)])
        return memo[jump]