class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        positive = -1 if x < 0 and n%2==1 else 1
        result = 1
        frac = 1 if n < 0 else 0
        x,n = abs(x),abs(n)
        while n > 0:
            if n % 2 == 1:
                result *= x
            x*=x
            n >>= 1
        if frac:
            return 1 / result * positive
        else:
            return result * positive
        