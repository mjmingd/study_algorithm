# Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
    '''
    time complexity : O(N)
    space complexity : O(N)
    '''
    
        if n == 1:
            return n
        if n == 2 :
            return 2
        
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 2
        for i in range(2, n) :
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n-1]
            
        
        
