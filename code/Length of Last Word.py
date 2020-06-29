class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        s_cut = s.split(' ')
        for i in s_cut[::-1]:
            if len(i) > 0:
                return len(i)
        return result