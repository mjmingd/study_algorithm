'''
Codility - Brackets

A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
'''


def isValid(s, last) :
    if s == ')' and last == '(' : return True
    if s == '}' and last == '{' : return True
    if s == ']' and last == '[' : return True
    return False
    

def solution(S):
    '''
    time complexity : O(N)
    space complexity : O(N)
    '''

    if not S : return 1
    stack = list()
    
    for s in S :
        if s in ['(','{','['] :
            stack.append(s)
        else :
            if len(stack) == 0 : return 0
            last = stack.pop()
            if not isValid(s,last) : return 0

    return 0 if len(stack) > 0 else 1
