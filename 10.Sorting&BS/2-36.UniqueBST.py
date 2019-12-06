# Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/

from collections import defaultdict
class Solution:
    def numTrees(self, n: int) -> int:
    '''
    time complexity : O(N^2)
    space complexity : O(N)
    '''
        if n ==1 : return 1
        dp = defaultdict(int)
        dp[0], dp[1] = 1, 1
        
        for i in range(2,n+1) :
            for j in range(1, i+1) :
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
