# Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS1(self, nums: List[int]) -> int:
    '''
    time complexity : TLE
    space complexity : 
    '''
    
        if not nums : return 0
        
        def helper(idx, LIS=[]) :
            while idx < len(nums):
                if LIS[-1] < nums[idx] :
                    helper(idx+1, LIS + [nums[idx]])
                else :
                    helper(idx+1, LIS)
            return len(LIS)
        
        ans = 0
        for i in range(len(nums)) :
            ans = max(ans, helper(i, [nums[i]]))
        
        return ans
