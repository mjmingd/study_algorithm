# Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    '''
    time complexity : O(MN)
    space complexity : O(1)
    '''
    
        def func(l, r, t, b) :
            i, j = t, l
            while j < r :
                ret.append(matrix[i][j])
                j += 1

            while i < b :
                ret.append(matrix[i][j])
                i += 1

            i = b
            while j > l  :
                ret.append(matrix[i][j])
                j -= 1
                
            j = l
            while i > t :
                ret.append(matrix[i][j])
                i -= 1
        
        ret = []
        if not matrix : return ret
        l, r, t, b = 0, len(matrix[0])-1, 0, len(matrix)-1
        while l<r and t<b:
            func(l, r, t, b)
            l, r, t, b = l+1, r-1, t+1, b-1
            
        if l == r and t==b :
            ret.append(matrix[t][l])
        else :
            if l == r :
                for i in range(t,b+1) :
                    ret.append(matrix[i][l])
            if t == b :
                for j in range(l,r+1) :
                    ret.append(matrix[t][j])
                
        return ret

