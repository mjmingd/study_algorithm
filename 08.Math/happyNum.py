# Happy Number
# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
    """
    time complextiy : O(?)
    space complexity : O(1)
    """
        sets = set()
        while n != 1 :
            n = sum([int(l)**2 for l in str(n)])
            if n not in sets :
                sets.add(n)
            else :
                return False
        return True
        
            
        
