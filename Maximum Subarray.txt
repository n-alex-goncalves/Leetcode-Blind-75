class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        INPUT: integer array nums
        OUTPUT: the sum of the largest contiguous subarray
        SOLUTION:    
        '''
        max_sum, right, cur_sum, num_len = nums[0], 0, 0, len(nums)
        if (num_len == 1): return nums[0]
        
        while (right < num_len):
            cur_sum = cur_sum + nums[right]
            max_sum = max(max_sum, cur_sum)
            if cur_sum < 0:
                cur_sum = 0
            right += 1
        
        return max_sum