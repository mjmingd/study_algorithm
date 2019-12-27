# Couples Holding Hands
# https://leetcode.com/problems/couples-holding-hands/


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
    '''
    time complexity : O(N)
    space complexity : O(N)
    '''
    
        seats = {x : idx for idx, x in enumerate(row)}
        ans = 0
        
        for idx in range(len(row)) :
            x = row[idx]
             
            if x % 2 == 0 :
                y = x + 1
            else :
                y = x - 1
            
            y_idx = seats[y]
            
            if abs(idx - y_idx) > 1 :
                row[y_idx], row[idx+1] = row[idx+1], row[y_idx]
                seats[row[idx+1]], seats[row[y_idx]] = idx+1, y_idx
                ans += 1
            
        return ans
                
