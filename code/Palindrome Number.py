class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        result = 0
        origin = x
        while x != 0:
            var = x % 10
            x = x // 10
            result = result * 10 + var
        if origin == result:
            return True
        else:
            return False