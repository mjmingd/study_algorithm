# Game of Life
# https://leetcode.com/problems/game-of-life/
# condition : Do not return anything, modify board in-place instead.

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        '''
        time complexity : O(MN)
        space complexity : O(MN)
        '''

        row, col = len(board), len(board[0])
        
        # tmp에 0으로 padding
        tmp  = []
        tmp.append([0]*(row+2))
        for r in board :
            tmp.append([0]+r+[0])
        tmp.append([0]*(row+2))
        
        
        for r in range(1,row+1) :
            for c in range(1,col+1) :
                # negihbor의 live cell 수를 구함
                cond = sum(tmp[r-1][c-1:c+2]) + sum(tmp[r][c-1 : c+2]) + sum(tmp[r+1][c-1:c+2]) - tmp[r][c]
                
                # 조건에 맞게 설정
                if tmp[r][c] == 1 :
                    if cond != 2 and cond != 3 :
                        board[r-1][c-1] = 0
                else :
                    if cond == 3 :
                        board[r-1][c-1] = 1
