# Validate Stack Sequences
# https://leetcode.com/problems/validate-stack-sequences/

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        
        stack = []
        i = 0
        for p in pushed :
            stack.append(p)
            while stack and stack[-1]==popped[i] :
                stack.pop()
                i += 1
        return len(stack) == 0 
