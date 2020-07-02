class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        for i in range(n):
            first = result
            second = [(1<<i)+num for num in result[::-1]]
            result = first+second
        return result