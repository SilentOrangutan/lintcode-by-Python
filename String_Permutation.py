# 两个字符串可置换，即字符串所包含的字符及其个数均相等
# 若两个均为空则亦相等,若一个字符串为空则不等




class Solution:
    """
    @param: A: a string
    @param: B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        # write your code here
        if len(A)==0 and len(B)==0:
            return True
        elif (len(A)==0 or len(B)==0):
            return False
        else:
            for i in A:
                if (i in B)and(A.count(i)==B.count(i)):
                    continue
                else:
                    return False
            return True
                
                