# single number 2
# https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    """
    time complexity : O(N)
    space complexity : O(N)
    """
    
        ret = {}
        for n in nums :
            if n not in ret :
                ret[n] = 1
            else :
                ret[n] += 1
        for k,v in ret.items():
            if v == 1 : 
                return k
