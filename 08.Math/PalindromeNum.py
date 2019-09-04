# Palindrome Number
# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome2(self, x: int) -> bool:
        """
        time complexity : O(log10(N))
        space complexity : O(1)
        """
        
        tmp, ans = x, 0
        if x < 0 :
            return False
        while tmp > 0 :
            ans = ans*10 + tmp % 10
            tmp = tmp//10
        return True if x == ans else False
    
    def isPalindrome1(self, x: int) -> bool:
        """
        time complexity :O(N)
        space complexity : O(1)
        """
        if x < 0 :
            return False
        x = str(x)
        return True if x == x[::-1] else False

        
