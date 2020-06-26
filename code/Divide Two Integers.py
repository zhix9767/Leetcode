class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2**31 and divisor == -1:
            return 2**31 -1
        positive = (dividend < 0) ^ (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        temp = divisor
        i = 1
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                i <<= 1
                temp <<= 1
            result += i >> 1
            dividend -= temp >> 1
        if positive:
            result = -result 
        return result