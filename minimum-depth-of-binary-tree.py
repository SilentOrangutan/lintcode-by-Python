# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     minimum-depth-of-binary-tree
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
    @param: root: The root of binary tree
    @return: An integer
    """
    # def minDepth(self, root):
    #     '''
    #     错误代码 if else 使用不当 导致return无法正确执行
    #     :param root:
    #     :return:
    #     '''
    #     # write your code here
    #     if root is None:
    #         return 0
    #     Queue=list()
    #     Queue.append(root)
    #     depth=0
    #     while Queue != []:
    #         curQueSize=len(Queue)
    #         cp=0
    #         while cp < curQueSize:
    #             temp=Queue.pop(0)
    #             cp+=1
    #             if temp.left is not None:
    #                 Queue.append(temp.left)
    #             elif temp.right is not None:
    #                 Queue.append(temp.right)
    #             else:
    #                 return depth
    def minDepth(self, root):
        # write your code here
        if root is None:
            return 0
        Queue=list()
        Queue.append(root)
        depth=0
        while Queue != []:
            curQueSize=len(Queue)
            cp=0
            depth+=1
            while cp < curQueSize:
                temp=Queue.pop(0)
                cp+=1
                if temp.left:
                    Queue.append(temp.left)
                if temp.right:
                    Queue.append(temp.right)
                if temp.left is None and temp.right is None:
                    return depth

