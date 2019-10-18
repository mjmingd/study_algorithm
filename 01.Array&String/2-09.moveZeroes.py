# Move Zeroes
# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes3(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0 
        for i in range(len(nums)):
            if nums[i] != 0 :
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
                
                
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        time complexity : O(NlogN)
        space complexity : O(1)
        """
        def sorting(n):
            return (0,) if n != 0 else (1,0)
        
        nums.sort(key= sorting)

        
    def moveZeroes1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0 
        for i in range(len(nums)-1) :
            i = i - count
            if nums[i] == 0 :
                count += 1
                nums.pop(i)
        
        nums.extend([0]*count)
