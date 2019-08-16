# Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root, less = float('inf'), greater=float('-inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
                    
        if root is None:
            return True
        if root.val <= greater or root.val >= less:
            return False
        return self.isValidBST(root.left, min(less, root.val), greater) and \
               self.isValidBST(root.right, less, max(root.val, greater))

