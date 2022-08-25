class Solution(object):
    def topKFrequent(self, nums, k):
        '''
        INPUT: interger array nums, k
        OUTPUT: return k most frequent elements
        '''
        
        numsDictionary = collections.defaultdict(int)
        
        for num in nums:
            numsDictionary[num] += 1
        
        numsFrequency = sorted([(num, numsDictionary[num]) for num in set(nums)], key = lambda x : x[1], reverse = True)
        return [x[0] for x in numsFrequency[:k]]