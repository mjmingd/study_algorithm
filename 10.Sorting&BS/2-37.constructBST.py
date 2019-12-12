# Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque
class Solution:
    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:    
        def helper(preorder, inorder) :
        '''
        time complexity : O(N)
        space complexity : O(N)
        '''
            if not inorder : return
            idx = inorder.index(preorder.popleft())
            root = TreeNode(inorder[idx])
            root.left = helper(preorder, inorder[:idx])
            root.right = helper(preorder, inorder[idx+1:])
            return root 
    
        preorder = deque(preorder)
        return helper(preorder, inorder)
        
        
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    '''
    time complexity : O(N)
    space complexity : O(N)
    '''
        if not inorder : return
        idx = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[idx])
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        return root 
        
