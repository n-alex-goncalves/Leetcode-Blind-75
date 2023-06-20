class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        INPUT: string s
        OUTPUT: true if palindrome, false if not
        NOTE:
        
        ignore spaces,
        ignore commas
        contains numbers
        
        SOLUTION:
        
        """
        s_list = [i.lower() for i in s if i.isalnum()]
        
        s_len = len(s_list)
        mid = s_len // 2
        for i in range(mid):
            if s_list[i] != s_list[s_len - i - 1]: return False
        
        return True