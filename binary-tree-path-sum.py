# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     binary-tree-path-sum
   Description :
   Author :       spongo
   date：          2017/11/18
-------------------------------------------------
   Change Activity:
                   2017/11/18:
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
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        result=[]
        if root is None:
            return []
        curNum=target-root.val
        if curNum==0 and root.left is None and root.right is None:
            result.append([root.val])
        if root.left is not None:
            result.extend(self.path(root.val,self.binaryTreePathSum(root.left,curNum)))
        if root.right is not None:
            result.extend(self.path(root.val,self.binaryTreePathSum(root.right,curNum)))
        return result




    def path(self,val,pathes):
        res=[]
        for path in pathes:
            res.append([val]+path)
        return res
