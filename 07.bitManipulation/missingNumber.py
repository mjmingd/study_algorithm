# Missing Number
# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
    """
    time complexity : O(N)
    space complexity : O(1)
        res = len(nums)
        for i, n in enumerate(nums) :
            res ^= i ^ n
        return res
            
         
