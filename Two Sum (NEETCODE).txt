class Solution(object):
    def twoSum(self, nums, target):
        '''
        INPUT: nums and target
        OUTPUT: indices of two numbers such that they add up to target
        NOTE:
        
        we can assume that each input has exactly onbe solution
        can't use the same element twice
        answer in any order
        
        SOLUTION:
        
        hashmap
        
        key element that we want : indice of the element that we know
        
        a + b = target
        
        key b : indice of a
        
        iteration
        
        '''
        
        numsDictionary = dict()
        
        for index, num in enumerate(nums):
            if num in numsDictionary and numsDictionary[num] != index:
                return [index, numsDictionary[num]]
            else:
                numsDictionary[target - num] = index
        
        return -1