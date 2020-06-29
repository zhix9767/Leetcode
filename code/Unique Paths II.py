class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, len(obstacleGrid)):
            dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])
        for i in range(1, len(obstacleGrid[0])):
            dp[0][i] = dp[0][i-1] * (1 - obstacleGrid[0][i])
        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) * (1 - obstacleGrid[i][j])
        return dp[-1][-1]