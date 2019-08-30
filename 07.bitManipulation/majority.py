# Majority Element
# https://leetcode.com/problems/majority-element/

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        time complexity : O(N)
        space complexity : O(N)
        """
        
        c = Counter(nums)
        return max(c.keys(), key = c.get)
        
