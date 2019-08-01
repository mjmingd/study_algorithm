# find Kth Largest Element in a Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minus = [-x for x in nums]
        heapq.heapify(minus)
        for i in range(k):
            a = heapq.heappop(minus)
        return -a
