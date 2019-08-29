# finde Single Number
# https://leetcode.com/problems/single-number/

class Solution:
    
    def singleNumber(self, nums: List[int]) -> int:
    """
    time complexcity : O(N)
    space complexcity : O(1)
    """
        res = 0
        for n in nums :
            res ^= n
        return res
   
    
    def singleNumber2(self, nums: List[int]) -> int:
    """
    time complexcity : O(N)
    space complexcity : O(N)
    """
        ret = {}
        for n in nums :
            if n not in ret :
                ret[n] = 1
            else :
                ret[n] += 1
        
        for k,v in ret.items() :
            if v == 1 :
                return k
    
    
    def singleNumber1(self, nums: List[int]) -> int:
        
        ret = []
        for n in nums :
            if n not in ret :
                ret.append(n)
            else :
                ret.remove(n)
        return ret.pop()
