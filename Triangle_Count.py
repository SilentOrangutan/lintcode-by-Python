#encoding=utf-8
# 三次循环会导致Time Limit Exceeded
# 先将数组sort排序，进行两次循环，通过二分法获得它们的差的位置，那么该位置到
# 最大值的位置应该都能满足要求，最后输出count


class Solution:
    """
    @param: S: A list of integers
    @return: An integer
    """

    def triangleCount(self, S):
        # write your code here
        if len(S) < 3:
            return
        count = 0
        S.sort()
        for i in range(0, len(S)):
            for j in range(i + 1, len(S)):
                l, r = i + 1, j
                tar = S[j] - S[i]
                while l < r:
                    mid = (l + r) // 2
                    mid_num=S[mid]
                    if mid_num > tar:
                        r = mid
                    else:
                        l = mid + 1
                count +=(j - l)
        return count


s = Solution()
print (s.triangleCount([3,4,6,7]))
