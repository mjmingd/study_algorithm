# Bitwise AND of Numbers Range
# https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
    """
    time complexity : O(1)
    space complexity : O(1)
    """
    
        c = 0
        while m != n :
            m >>= 1
            n >>= 1
            c += 1
        return n << c
