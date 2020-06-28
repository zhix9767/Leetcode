class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n == 0:
            return []
        result = []
        position = [-1] * n
        self.dfs(position,0,result)
        return result

    def dfs(self, position, n, result):
        if n == len(position):
            ans = []
            for i in range(len(position)):
                ans.append('.'*position[i] + 'Q' + '.'*(len(position)-position[i]-1))
            result.append(ans)
        for i in range(len(position)):
            if self.isValid(position,n,i):
                position[n] = i
                self.dfs(position,n+1,result)

    def isValid(self, position, n, new_position):
        for i in range(n):
            if new_position == position[i] or n-i == abs(position[i]-new_position):
                return False
        return True