#先计算出个点到origin的距离，然后利用数组的sort方法进行排序，最后输出


class Solution:
    """
    @param: points: a list of points
    @param: origin: a point
    @param: k: An integer
    @return: the k closest points
    """

    def kClosest(self, points, origin, k):
        # write your code here
        s = []
        t = []
        for i in range(len(points)):
            x = self.caculat(points[i], origin)
            s.append([x, points[i][0], points[i][1]])
        s.sort()  # s内部嵌套数组[距离，x坐标，y坐标]，sort方法会依（距离，x，y）自动比较
        for i in range(len(s)):
            t.append([s[i][1], s[i][2]])
        if k >= len(t):
            return t
        else:
            return t[:k]

    def caculat(self, s, b):
        l = ((s[0] - b[0])**2 + (s[1] - b[1])**2)**0.5
        return l


s = Solution()
print (s.kClosest([[4, 6], [4, 7], [4, 4], [2, 5], [1, 1]], [0, 0], 3))


#Result:[[4,6],[4,7],[4,4],[2,5],[1,1]]
