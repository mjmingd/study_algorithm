# Move Zeroes
# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        time complexity : O(NlogN)
        space complexity : O(1)
        """
        def sorting(n):
            return (0,) if n != 0 else (1,0)
        
        nums.sort(key= sorting)
