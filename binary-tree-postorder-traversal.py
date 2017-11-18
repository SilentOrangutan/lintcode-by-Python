# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     binary-tree-postorder-traversal
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
    @return: Postorder in ArrayList which contains node values.
    """
    result=[]
    def postorderTraversal(self, root):
        '''
        递归实现
        :param root:
        :return:
        '''
        # write your code here
        if root is not None:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.result.append(root.val)
        return self.result

    def postorderTraversal01(self, root):
        '''
        非递归实现
        :param root:
        :return:
        '''
        p=[] #栈
        res=[] #输出数组
        past=None #上次访问节点
        while root is not None:
        #将root移至最左子树最下端
            p.append(root)
            root=root.left
        while p !=[]:
            root=p.pop()
            if root.right is None or root.right==past:#一个根节点被输出的条件是：右子树为空或右子树已经访问过
                res.append(root.val)
                past=root #变更上次访问节点
            else:#root无法输出说明root节点存在右子树且未被访问过
                p.append(root) #root再次入栈
                root=root.right #将root移至右子节点
                while root is not None:
                    p.append(root)
                    root=root.left
        return res

