# finde Single Number
# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = {}
        for n in nums :
            if n not in ret :
                ret[n] = 1
            else :
                ret[n] += 1
        
        for k,v in ret.items() :
            if v == 1 :
                return k
