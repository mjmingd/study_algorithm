# Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
    '''
    time complexity : O(mn)
    space complexity : O(n)
    '''
    
        if len(grid) == 0 :
            return grid

        r, c = len(grid), len(grid[0])
        
        tmp1 = tmp2 = [0] * c
        tmp1[0] = grid[0][0]
        
        for i in range(1, c) :
            tmp1[i] = tmp1[i-1] +  grid[0][i]
            
        for i in range(1, r) :
            tmp2[0] = tmp1[0] + grid[i][0]
            for j in range(1,c):
                tmp2[j] = min(tmp1[j], tmp2[j-1]) + grid[i][j]
            tmp1 = tmp2
        
        return tmp2[-1]
