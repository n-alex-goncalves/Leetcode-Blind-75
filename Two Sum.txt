class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        INPUT: array of itnegers nums and an integer target
        OUTPUT: return indicies of two number such that they add up to target
        SOLUTION:
        
        hashmap key:item, key - difference 
        key: target - num[i]
        item: index i
        
        for loop:
            is the num[i] in the hashmap
                we have two numbers, i and j, where i is the difference key - num[j]
                therefore, num[i] + num[j] = target
            else
                we just add the difference (or what we need) to the hashmap
                
        time complexity of O(n)
        space complexity of O(n)
        '''
        
        dictionary = dict()
        
        for i in range(0, len(nums)):
            if nums[i] in dictionary:
                return [i, dictionary[nums[i]]]
            else:
                dictionary[target - nums[i]] = i
        
        return []