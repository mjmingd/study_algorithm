# House Robber
# https://leetcode.com/problems/house-robber/

from collections import defaultdict

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums : return 0
        if len(nums) <= 2 : return max(nums)
        
        dp = defaultdict(int)
        
        for i in range(len(nums)) :
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
            
        return max(dp.values())
