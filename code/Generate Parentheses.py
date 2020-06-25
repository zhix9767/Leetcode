class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def generateParenthesis2(Str = "", left = 0, right = 0):
            if len(Str) == 2*n:
                result.append(Str)
            if left < n:
                generateParenthesis2(Str+'(',left + 1, right)
            if right < left:
                generateParenthesis2(Str + ')',left, right + 1)
        generateParenthesis2()
        return result