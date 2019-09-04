# Reverse Integer
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
    """
    time complexity : O(log10((N))
    space complexity : O(1)
    """
        ans , sign = 0, 1
        if x < 0 :
            sign = -1
            x = sign * x
        while x > 0 :
            ans = ans*10 + x % 10
            x = x//10
        return sign * ans if sign * ans in range(-(2**31), 2**31-1) else 0
            
        
            
        
