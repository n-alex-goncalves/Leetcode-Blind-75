class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = dict()
        
        for num in nums:
            if num in dictionary:
                return True
            else:
                dictionary[num] = num
        
        return False