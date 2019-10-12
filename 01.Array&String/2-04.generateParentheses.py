# Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    '''
    time complexity : O()
    space complexity : O()
    '''
        ret = []
        prev, left, right ='', 0, 0
        def func(prev, left, right) :
            if len(prev) == 2 * n :
                ret.append(prev)
                return
            if left < n :
                func(prev + '(', left+1, right)
            if right < left :
                func(prev + ')', left, right+1)
        
        func(prev, left, right)
        return ret
        
