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
        