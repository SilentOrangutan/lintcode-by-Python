# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     maximum-depth-of-binary-tree
   Description :
   Author :       spongo
   date：          2017/11/20
-------------------------------------------------
   Change Activity:
                   2017/11/20:
-------------------------------------------------
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0
        else:
            leftDepth=self.maxDepth(root.left)
            rightDepth=self.maxDepth(root.right)
        return leftDepth+1 if leftDepth>rightDepth else rightDepth+1