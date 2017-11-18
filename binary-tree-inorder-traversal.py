#encoding:utf-8
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
    @return: Inorder in ArrayList which contains node values.
    """

    result=[]
    
    def inorderTraversal(self, root):
        '''
        递归解法
        :param root:
        :return:
        '''
        # write your code here
        if root != None:
            self.inorderTraversal(root.left)
            self.result.append(root.val)
            self.inorderTraversal(root.right)
        return self.result

    def inorderTraversal01(self,root):
        '''
        非递归实现
        :param root:
        :return:
        '''
        p = []
        res = []
        while root is not None or p != []:
            while root is not None:
                p.append(root)
                root = root.left
            root = p.pop(-1)
            res.append(root.val)
            root=root.right
        return res

