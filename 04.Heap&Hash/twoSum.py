# Two Sum
# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        nums_d = {}
        for i, n in enumerate(nums) :
            diff = target - n
            if diff in nums_d:
                return [nums_d[diff], i]
            else :
                nums_d[n] = i
