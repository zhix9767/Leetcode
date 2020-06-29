class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        result = [[0] * n for _ in range(n)]
        temp = 1
        up, down, left, right = 0, n, 0, n
        while temp <= n**2:
            if down - up == 1:
                result[up][up] = temp
                temp += 1
                continue
            for i in range(left,right):
                result[up][i] = temp
                temp += 1
            for i in range(up+1,down):
                result[i][right-1] = temp
                temp += 1
            for i in range(right-2,left-1,-1):
                result[down-1][i] = temp
                temp += 1
            for i in range(down-2,up,-1):
                result[i][left] = temp
                temp += 1
            up, down, left, right = up+1, down-1, left+1, right-1
        return result
