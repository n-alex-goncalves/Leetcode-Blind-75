class Solution(object):
    def containsDuplicate(self, nums):
        '''
        INPUT: nums - integer array
        OUTPUT: boolean value - true if any value appears twice and false if not
        SOLUTION:
        
        hashmap = dict()
        
        for element in nums
        if element in hashmap:
            retrun true
        else:
            return false
        
        time complexity: O(n)
        space complexity: O(n)
        '''
        
        numDictionary = dict()
        
        for num in nums:
            if num in numDictionary:
                return True
            else:
                numDictionary[num] = None
        
        return False