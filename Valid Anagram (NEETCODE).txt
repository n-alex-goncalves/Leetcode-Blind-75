class Solution(object):
    def isAnagram(self, s, t):
        '''
        INPUT: s and t - strings
        OUTPUT: return true if t is an anagram of s, otherwise false
        SOLUTION:
        
        all the letters of s == all the letters of t (including duplicates)
        
        sDictionary = dict()
        
        key letter : value number of letter
        
        '''
        
        sDictionary = dict()
        
        for letter in s:
            if letter in sDictionary:
                sDictionary[letter] += 1
            else:
                sDictionary[letter] = 1
        
        for letter in t:
            if letter in sDictionary and sDictionary[letter] > 0:
                sDictionary[letter] -= 1
            else:
                return False
        
        return all([x == 0 for x in sDictionary.values()])