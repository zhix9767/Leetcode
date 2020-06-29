class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        add  = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += add
            add = digits[i] // 10
            digits[i] %= 10
        if add:
            digits = [1] + digits
        return digits
