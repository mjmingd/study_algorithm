# Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS2(self, nums: List[int]) -> int:
        '''
        time complexity : O(N^2)
        space complexity : O(N)
        '''
        
        if not nums : return 0
        dp = [1 for _ in nums]
        _len = len(nums)
        
        for i in range(_len) :
            _max = 0
            for j in range(i) :
                if nums[j] < nums[i] :
                    _max = max(dp[j], _max)
            dp[i] = _max + 1
        
        return max(dp)
    
    
    
    
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
