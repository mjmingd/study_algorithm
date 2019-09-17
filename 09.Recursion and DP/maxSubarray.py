# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    """
    time complexity : O(N)
    space complexity : O(1)
    """
    
        if not nums :
            return 0
        sum, maxSum = 0, nums[0]
        for n in nums :
            sum = max(n, sum + n)
            maxSum = max(maxSum, sum)
        return maxSum
