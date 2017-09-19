class Solution:
    # @return: The same instance of this class every time
    _m_Solution = None
    @classmethod
    def getInstance(self):
        # write your code here
        if self._m_Solution==None:
            self._m_Solution=Solution()
        return self._m_Solution

