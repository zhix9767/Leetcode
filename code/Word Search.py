class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not self.preCheck(board, word):
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(i,j,board,word):
                    return True
        return False
        
    def dfs(self, i, j, board, word):
        if len(word) == 0:
            return True
        if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0 or board[i][j]!=word[0]:
            return False
        temp = board[i][j]
        board[i][j] = ' '
        result =  self.dfs(i+1,j,board,word[1:]) or self.dfs(i-1,j,board,word[1:]) or self.dfs(i,j-1,board,word[1:]) or self.dfs(i,j+1,board,word[1:])
        board[i][j] = temp
        return result

    def preCheck(self,board,word):
        dic={}

        for i in word:
            dic[i]=dic.get(i,0)+1
        for i in board:
            for j in i:
                if j in dic and dic[j]>0: dic[j]-=1
        for i in dic.values():
            if i>0: return False
        return True