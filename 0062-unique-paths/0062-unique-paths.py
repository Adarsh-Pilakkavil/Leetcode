class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[float("inf") for j in range(n)]for i in range(m)]
        def rec(dp,i,j):
            if i==m-1 or j==n-1:
                return 1
            if dp[i][j]!=float("inf"):
                return dp[i][j]
            dp[i][j]=rec(dp,i+1,j)+rec(dp,i,j+1)
            return dp[i][j]
        return rec(dp,0,0)