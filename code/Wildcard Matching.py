class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        for j in range(1, len(p)+1):
            if p[j-1] != '*':
                break
            dp[0][j] = True
                
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] in {s[i-1], '?'}:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i-1][j-1] or dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]

    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        j = 0

        star = -1 
        matched_end = -1

        while i < len(s):
            if j < len(p) and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                matched_end = i
                star = j
                j += 1
            else:
                if star > -1:
                    matched_end += 1
                    i = matched_end
                    j = star + 1           
                else:
                    return False 
        
        while j < len(p):
            if p[j] != '*':
                return False
            j += 1 

        return True
        
    def isMatch3(self, s, p):
        p_cut = p.split('*')
        location = 0
        for i in range(len(p_cut)):
            p_cut2 = p_cut[i].split("?")
            for j in range(len(p_cut2)):
                if i == 0 and j == 0:
                    if self.strStr(s[location:len(s)], p_cut2[j]) != 0:
                        return False
                    location = len(p_cut2[j]) + 1
                elif i == len(p_cut) - 1 and j == len(p_cut2) - 1:
                    if location > len(s)-len(p_cut2[j]) or \
                        self.strStr(s[len(s)-len(p_cut2[j]):len(s)], p_cut2[j]) != 0:
                        return False
                else:
                    temp = self.strStr(s[location:len(s)], p_cut2[j])
                    if temp == -1:
                        return False
                    location += len(p_cut2[j]) + temp + 1
            location -= 1
        if len(p_cut) == 1 and len(s) != len(p):
            return False
        return True
            


    def strStr(self, haystack, needle):
        if len(needle) == 0:
            return 0
        if len(haystack) == 0:
            return -1

        pmt = [0] * len(needle)
        pmt[0] = 0
        maxLength = 0
        for i in range(1, len(needle)):
            while maxLength > 0 and needle[i] != needle[maxLength]:
                maxLength = pmt[maxLength-1]
            if needle[i] == needle[maxLength]:
                maxLength += 1
            pmt[i] = maxLength

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
s = "accab"
p = "c?b"
print(test.isMatch3(s,p))