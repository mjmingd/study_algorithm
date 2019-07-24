# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # using stack
        stack = []
        mapping = {')' : '(', '}' : '{', ']' : '['}
        
        # empty string is also valid
        if s == '' :
            return True
            
        # start with closed parentheses is not valid
        if s[0] in mapping.keys() :
            return False
        
        for p in s :
            if p in mapping.values():
                stack.append(p)
            elif p in mapping.keys() :
                if stack == []  or mapping[p] != stack.pop() :
                    return False
        if stack != [] :
            return False
        
        return True
                    
                    
                
            

