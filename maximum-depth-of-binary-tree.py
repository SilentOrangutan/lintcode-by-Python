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
        '''
        递归实现1
        :param root:
        :return:
        '''
        # write your code here
        if root is None:
            return 0
        else:
            leftDepth=self.maxDepth(root.left)
            rightDepth=self.maxDepth(root.right)
        return leftDepth+1 if leftDepth>rightDepth else rightDepth+1

    def maxDepth01(self,root):
        '''
        递归实现2
        :param root:
        :return:
        '''
        depth=0
        if root is not None:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)
            depth=leftDepth+1 if leftDepth>rightDepth else rightDepth+1
        return depth

    def maxDepth02(self,root):
        '''
        非递归实现
        :param root:
        :return:
        '''
        if root is None:
            return 0
        depth=0
        Queue=list() #Queue储存当前及下层的节点
        Queue.append(root)
        while Queue != []: #每次循环代表上层pop完毕，开始本层pop
            depth+=1
            curQueSize=len(Queue) #代表当前层的节点个数
            cp=0 #指针
            while cp < curQueSize:
                #将本层的节点全部pop
                temp=Queue.pop(0) #FIFO
                cp+=1
                #将下层节点加入队列
                if temp.left is not None:
                    Queue.append(temp.left)
                if temp.right is not None:
                    Queue.append(temp.right)
        return depth
