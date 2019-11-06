# Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator: #recursion
    ''' 
    time complexity : O(N)/ O(1)/ O(1)
    space complexity : O(N)
    '''
    
    def __init__(self, root: TreeNode):
        self.dec = deque()
        self.inorder(root)
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.dec.popleft()
        
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return True if self.dec else False
            
    def inorder(self, root) :
        if not root : return
        self.inorder(root.left)
        self.dec.append(root.val)
        self.inorder(root.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
