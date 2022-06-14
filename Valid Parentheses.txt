class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = dict()
        dictionary['('] = ')'
        dictionary['{'] = '}'
        dictionary['['] = ']'
        stack = []
        for i in s:
            if i in dictionary:
                stack.append(dictionary[i])
            elif len(stack) == 0 or i != stack.pop():
                return False
        
        return True if len(stack) == 0 else False
                