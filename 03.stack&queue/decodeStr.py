# decode string
# https://leetcode.com/problems/decode-string/

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_stack = list()
        num = curNum = 0
        pattern = ''
        
        for c in s :
            if c.isdigit() :
                curNum = curNum*10 + int(c)
                
            elif c == '[':
                str_stack.append(pattern) 
                str_stack.append(curNum)
                curNum = 0
                pattern = ''
                
            elif c == ']' :
                num = str_stack.pop()
                prev = str_stack.pop()
                pattern = prev + pattern * num
                
            else :
                pattern += c
                
        return pattern
                
                
