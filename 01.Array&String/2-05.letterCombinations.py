# Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
    '''
    time complexity : O(O(3^N * 4^M)
    space complexity : O(3^N * 4^M))
    '''
    
        num2char = {'2':['a','b','c'],
                    '3':['d','e','f'],
                    '4':['g','h','i'],
                    '5':['j','k','l'],
                    '6':['m','n','o'],
                    '7':['p','q','r','s'],
                    '8':['t','u','v'],
                    '9':['w','x','y','z']}
        
        def func(combination, digits) :
            if len(digits) == 0 :
                ret.append(combination)
            else :
                for char in num2char[digits[0]] :
                    func(combination + char, digits[1:])
        
        ret = []
        if digits :
            func('', digits)
        return ret
        
        
