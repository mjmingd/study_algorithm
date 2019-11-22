# Burst Balloons
# https://leetcode.com/problems/burst-balloons/

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
    """
    time complexity : O(N^3)
    space complexity : O(N^2)
    """
    
        if not nums : return 0
        nums = [1] + nums +[1]
        dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        
        def helper(left, right) :
            if dp[left][right] or right == left + 1 : return dp[left][right]
            ans = 0
            for i in range(left+1, right) :
                ans = max(ans, nums[left]*nums[i]*nums[right]+helper(left,i)+helper(i,right))
            dp[left][right] = ans
            return ans
        
        return helper(0, len(nums)-1)
            
