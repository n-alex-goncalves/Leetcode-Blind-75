class Solution(object):
    def groupAnagrams(self, strs):
        '''
        INPUT: strs
        OUTPUT: list of list of strings
        SOLUTION:
        
        
        iteration
        count 
        
        
        stringDictionary = collections.defaultdict(list)
        
        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1
            stringDictionary[tuple(count)].append(string)
        
        return stringDictionary.values()
        
        '''
        stringDictionary = collections.defaultdict(list)
        
        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1
            stringDictionary[tuple(count)].append(string)
        
        return stringDictionary.values()