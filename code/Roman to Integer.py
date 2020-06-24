class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        result = 0
        for i in range(len(s)):
            if i < len(s)-1 and dic[s[i]]<dic[s[i+1]]:
                result -= dic[s[i]]
            else:
                result += dic[s[i]]
        return result