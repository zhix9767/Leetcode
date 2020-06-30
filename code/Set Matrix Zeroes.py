class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        Col = False
        Row = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                Row = True
                break
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                Col = True
                break
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if Row:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if Col:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        return