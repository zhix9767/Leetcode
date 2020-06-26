class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1

        # calculate partial match table
        pmt = [0] * len(needle)
        pmt[0] = 0
        maxlength = 0
        for i in range(1,len(needle)):
            while maxlength > 0 and needle[i] != needle[maxlength]:
                maxlength = pmt[maxlength-1]
            if needle[i] == needle[maxlength]:
                maxlength += 1
            pmt[i] = maxlength
        
        count = 0
        for i in range(len(haystack)):
            while count > 0 and haystack[i] != needle[count]:
                count = pmt[count-1]
            if haystack[i] == needle[count]:
                count += 1
            if count == len(needle):
                return i - len(needle) + 1
        return -1

test = Solution()
haystack = "mississippi"
needle = "mississippi"
print(test.strStr(haystack,needle))
