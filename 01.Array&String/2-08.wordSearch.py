# Word Search
# https://leetcode.com/problems/word-search/


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
    """
    time complexity : O(MNS)
    space complexity : O(S)
    """
    
        def dfs(i, j, word) :
            if len(word) == 0: # all the characters are checked
                    return True
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                    return False
            if word[0]!=board[i][j] :
                return False
            tmp, board[i][j] = board[i][j], "" 
            res = dfs(i+1, j, word[1:]) or dfs(i-1, j, word[1:]) or dfs(i, j+1, word[1:]) or dfs(i, j-1, word[1:])
            board[i][j] = tmp
            return res


        if not board :
            return False

        for i in range(len(board)):
            for j in range(len(board[0])) :
                if dfs(i, j, word) : return True
        return False
                
            
        
