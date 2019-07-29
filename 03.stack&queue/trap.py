# trapping rain water
# https://leetcode.com/problems/trapping-rain-water/

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left_max = right_max = water = 0
        left = []
        right = []
        
        # tracking the highest wall ever seen (left -> right)
        for h in height :
            if h > left_max :
                left_max = h
            left.append(left_max)
            
        # tracking the highest wall ever seen (right -> left)   
        for h in reversed(height):
            if h > right_max :
                right_max = h
            right.append(right_max)
        right.reverse()
        
        # measuring water trapped that point    
        for i,h in enumerate(height) :
            water = water + (min(left[i], right[i]) - h)
            
        return water
