class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.rowValid(board) and self.colValid(board) and self.squareValid(board)

    def isUnitValid(self, nums):
        unit = [i for i in nums if i != '.']
        return len(unit) == len(set(unit))

    def rowValid(self, board):
        for i in board:
            if not self.isUnitValid(i):
                return False
        return True

    def colValid(self, board):
        for i in zip(*board):
            if not self.isUnitValid(i):
                return False
        return True
    
    def squareValid(self, board):
        for i in (0,3,6):
            for j in (0,3,6):
                square = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                if not self.isUnitValid(square):
                    return False
        return True