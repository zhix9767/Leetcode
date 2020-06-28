class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        n = len(matrix) // 2
        for i in range(n):
            for j in range(len(matrix)-n):
                matrix[i][j], matrix[j][len(matrix)-i-1], matrix[len(matrix)-i-1][len(matrix)-j-1], matrix[len(matrix)-j-1][i] = \
                matrix[len(matrix)-j-1][i],matrix[i][j], matrix[j][len(matrix)-i-1], matrix[len(matrix)-i-1][len(matrix)-j-1]
        return