class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        INPUT: two strings
        OUTPUT: true if anagram, false if not
        SOLUTION:
        dictionaries
        
        it's not simple just to chck if one letter is in the other,
        because you can have multiples
        i guess you can just pop them off? using what?
        remove() - removes first occurence
        
        perhaps you can use dictionaries?
        two for loops
        
        one to instantiate the dictionary
        the other to check for letters inside
        
        probably better than the latter solution because you wouldn't have to pop them off, which would requiring going
        through the array multiple times in an iteration.
        '''
        
        if len(s) != len(t): return False
        
        dictionary = dict()
        
        for i in s:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        
        for j in t:
            if j in dictionary:
                dictionary[j] -= 1
                if dictionary[j] < 0:
                    return False
            else:
                return False
        
        return True