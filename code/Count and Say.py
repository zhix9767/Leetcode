class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        result = "1"
        for _ in range(n-1):
            prev, temp, count = result[0], "", 0
            for i in result:
                if i == prev:
                    count += 1
                else:
                    temp += (str(count) + prev)
                    prev = i
                    count = 1
            result = temp + str(count) + prev
        return result
