class Solution:
    def canJump(self, nums: List[int]) -> bool:
        num_len = len(nums)
        table = [False for i in range(num_len)]
        table[num_len - 1] = True
        
        for i in range(num_len - 2, -1, -1):
            table[i] = any(table[i + 1:i + nums[i] + 1])
        
        return table[0]