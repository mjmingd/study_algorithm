# Maximal Square
# https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix : return 0
        row, col = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(col)] for _ in range(row)] 
        ret = 0

        for r in range(row):
            for c in range(col) :
                if int(matrix[r][c]) == 1 :
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])+1
                    ret = max(ret, dp[r][c])
        return ret*ret
        
                   
