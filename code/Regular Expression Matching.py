class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        matrix = [[False] * (len(p)+1) for _ in range(len(s)+1)]
        matrix[len(s)][len(p)] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                firstTry = (i < len(s) and p[j] in {'.',s[i]})
                if j+1 < len(p) and p[j+1] == '*':
                    matrix[i][j] = matrix[i][j+2] or (firstTry and matrix[i+1][j])
                else:
                    matrix[i][j] = firstTry and matrix[i+1][j+1]
        return matrix[0][0]