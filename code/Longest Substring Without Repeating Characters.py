class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = {}
        result = 0;
        loc = 0;
        for i in range(len(s)):
            if s[i] in index:
                loc = max(index.get(s[i]) + 1, loc)         
            index[s[i]]=i
            result = max(result, i-loc+1)
        return result

test=Solution()
print(test.lengthOfLongestSubstring("abba"))
                