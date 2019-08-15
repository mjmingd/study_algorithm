# Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def Check(left, right):
            if left is None and right is None :
                return True
            if left is None or right is None :
                return False
            if left.val == right.val :
                f1 = Check(left.left, right.right)
                f2 = Check(left.right, right.left)
                return f1 and f2
        
        
        if root == None :
            return True
        else :
            return Check(root.left, root.right)
