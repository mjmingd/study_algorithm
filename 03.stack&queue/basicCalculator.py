# Basic Calculator
# https://leetcode.com/problems/basic-calculator/

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = []
        num = Cnum = 0
        sign = 1
        
        for char in s :
            if char.isdigit() :
                Cnum = Cnum * 10 + int(char)
                
            elif char == '+' :
                num = num + Cnum * sign
                sign = 1
                Cnum = 0
                
            elif char == '-':
                num = num + Cnum * sign
                sign = -1
                Cnum = 0
                
            elif char == '(' :
                stack.append([num,sign])
                # rest values
                num = Cnum = 0
                sign = 1
                
            elif char == ')' :
                num = num + Cnum * sign
                Cnum, sign = stack.pop()
                num = Cnum + num * sign
                Cnum = 0 
        
        num = num + sign * Cnum
        
        return num
                
