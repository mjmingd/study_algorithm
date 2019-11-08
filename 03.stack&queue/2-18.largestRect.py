# Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# references : https://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-set-1/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
    '''
    time complexity : O(N)
    space complexity : O(N)
    '''
    
        if not heights : return 0
        
        h = len(heights)
        left, right = [1 for _ in range(h)], [1 for _ in range(h)]
        
        # 왼쪽에 나보다 같거나 큰면서 연속된 bar의 갯수
        for i in range(h) :
            p = i - 1
            while p >= 0 :
                if heights[i] <= heights[p] :
                    left[i] += left[p]
                    p -= left[p]
                else : break
                    
        # 오른쪽에 나보다 같거나 크면서 연속된 bar의 갯수
        for i in range(h-1, -1, -1) :
            p = i + 1 
            while p < h :
                if heights[i] <= heights[p] :
                    right[i] += right[p]
                    p += right[p]
                else : break
                    
        ret = 0
        for i in range(h) :
            ret = max(ret, (left[i] + right[i] - 1) * heights[i])
        return ret
        
        
            
