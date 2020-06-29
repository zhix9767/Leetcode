class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        cur = 2 **16
        for i in range(17):
            if (result + cur)**2 <= x:
                if (result + cur + 1)**2 > x:
                    return result + cur
                else:
                    result += cur
                    cur //= 2
            else:
                cur //= 2
        return result
                