# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     binary-tree-preorder-traversal
   Description :
   Author :       spongo
   date：          2017/11/18
-------------------------------------------------
   Change Activity:
                   2017/11/18:
    Refer:    http://blog.csdn.net/zhangxiangdavaid/article/details/37115355?reload
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
    @param: root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    result=[]
    def preorderTraversal(self, root):
        '''
        递归实现
        :param root:
        :return:
        '''
        # write your code here
        if root !=None:
            self.result.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.result

    def preorderTraversal01(self,root):
        '''
        非递归实现
        :param root:
        :return:
        '''
        p=[]
        res=[]
        while root is not None or p !=[]:
            while root is not None:
                p.append(root)
                res.append(root)
                root=root.left
            root=p.pop()
            root=root.right
        return res
