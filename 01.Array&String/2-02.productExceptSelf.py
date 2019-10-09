# Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    '''
    time complexity : O(N)
    space complexity : O(N)
    '''
        L, R, init = [], [], 1
        for n in nums :
            init *= n
            L += init,
        
        init = 1
        for rn in nums[::-1] :
            init *= rn
            R += init,

        R = R[::-1]
        ret = [R[1]]
        
        for i in range(len(nums)-2):
            ret.append(L[i]*R[i+2])
        ret.append(L[len(nums)-2])
        
        return ret
