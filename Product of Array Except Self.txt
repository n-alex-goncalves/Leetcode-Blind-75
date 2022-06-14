class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        INPUT: integer array nums
        OUTPUT: array such that answer[i] is the product of all elements of num except nums[i]
        SOLUTION:
        
        [->]
        [<-]
        
        [1,2,3,4]
        [->] = [1, 1, 2, 6]
        [<-] = [24, 12, 4, 1]
        
        everything before
        everything after
        
        num_len = len(nums)
        table = [1 for i in range(num_len)]
        product = 1
        for i in range(1, num_len):
            table[i] = product = product * nums[i - 1]
            
        
        
        
        
        '''
        num_len = len(nums)
        before, after, a_product, b_product = [1 for i in range(num_len)], [1 for i in range(num_len)], 1, 1
        for i in range(1, num_len):
            before[i] = b_product = b_product * nums[i - 1]
            after[num_len - i - 1] = a_product = a_product * nums[num_len - i]
    
        return [i * j for i, j in zip(before, after)]