class Solution(object):
    def productExceptSelf(self, nums):
        """
        INPUT: nums - integer array
        OUTPUT: answer - integer array such that answer[i] = product(nums except nums[i])
        SOLUTION:
        
        having a preNums and postNums
        
        for example...
        
        nums     = [1, 2, 3, 4]
        preNums  = [1, 1, 2, 6]
        postNums = [24, 12, 4, 1]
        
        ...the answer[i] is the multiple of preNums and postNums
        
        lenNums = len(nums)
        
        prefix  = [1] * lenNums
        postfix = [1] * lenNums
        
        for index in range(1, lenNums):
            preFix[index] *= nums[index - 1] 
            
        """
        
        lenNums = len(nums)
        prefix  = [1] * lenNums
        postfix = [1] * lenNums
        
        product = 1
        for index in range(1, lenNums):
            product *= nums[index - 1]
            prefix[index] = product
        
        product = 1
        for index in range(lenNums - 2, -1, -1):
            product *= nums[index + 1]
            postfix[index] = product
            
        return [x[0] * x[1] for x in zip(prefix, postfix)]
