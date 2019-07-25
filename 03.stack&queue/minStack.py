# Min Stack
# https://leetcode.com/problems/min-stack/

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.min == None :
            self.min = x
        if self.min > x :
            self.min = x
        self.stack.append([x, self.min])

    def pop(self):
        """
        :rtype: None
        """

        self.stack.pop()[0]
        if len(self.stack) == 0 :
            self.min = None
        else :
            self.min = self.getMin()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[len(self.stack)-1][1]
        
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
