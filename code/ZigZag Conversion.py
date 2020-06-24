class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) == 0:
            return ""
        if numRows == 1:
            return s
        count = 2 * numRows -2
        result = ""
        for i in range(numRows):
            for j in range(0, len(s)-i, count):
                result += s[i+j]
                if (i != 0 and i != numRows-1 and j+count-i<len(s)):
                    result += s[j+count-i]
        return result