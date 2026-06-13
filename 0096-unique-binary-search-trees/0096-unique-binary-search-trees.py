class Solution:
    def numTrees(self, n: int) -> int:
        dp=[0]*(n+1)
        if n==1:
            return 1
        dp[0]=1
        dp[1]=1
        for node in range(2,n+1):
            for i in range(1,node+1):
                dp[node]+=dp[node-i]*dp[i-1]
        return dp[-1]