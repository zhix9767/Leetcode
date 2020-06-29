class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        result = [0] * n
        result[0] = 1
        result[1] = 2
        for i in range(2, n):
            result[i] = result[i-1] + result[i-2]
        return result[-1]