# Palindrome Number
# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
    """
    time complexity :O(N)
    space complexity : O(1)
    """
        if x < 0 :
            return False
        x = str(x)
        return True if x == x[::-1] else False

        
