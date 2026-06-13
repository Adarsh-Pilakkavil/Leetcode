class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0-1]*n for _ in range(m)]
        def rec(i,j,dp,obstacleGrid):
            if i>=m or j>=n or obstacleGrid[i][j]:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=rec(i+1,j,dp,obstacleGrid)+rec(i,j+1,dp,obstacleGrid)
            return dp[i][j]
        return rec(0,0,dp,obstacleGrid)            