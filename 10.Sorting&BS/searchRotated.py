# Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search1(self, nums: List[int], target: int) -> int:
    # TLE
        def binary (s, median) :
            while abs(median - s) >= 1:
                if target in nums[s:median] :
                    median = s + len(nums[s:median])//2
                    binary(s, median)
                elif target in nums[median:] :
                    s = median
                    median = s + len(nums[median:])//2
                    binary(s, median)
                else :
                    return -1
                
            if nums[s] == target :
                return s
            elif nums[median] == target :
                return median
            else :
                return -1
            
        if nums == [] :
            return -1
        
        if len(nums) == 1 :
            return 0 if target in nums else -1
        
        median = len(nums)//2
        s = 0
        
        return binary(s, median)
        
            
        
        
