# Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
    '''
    time complexity : O(N)
    space complexity : O(N)
    '''
    
        if not T : return T
        stack, ret= [], [0 for i in range(len(T))]
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t :
                tmp_i = stack.pop()
                ret[tmp_i] = i - tmp_i
            stack.append(i)
        return ret
