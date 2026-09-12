class Solution:
    def numSquares(self, n: int) -> int:
        dp=[-1]*(n+1)
        dp[0]=0
        def rec(t,dp,c):
            if t==0:
                return c
            if dp[t]!=-1:
                return c+dp[t]
            k=float("inf")
            i=1
            while i<=int(t**0.5):
                k=min(k,rec(t-i**2,dp,c+1))
                i+=1
            dp[t]=k
            return dp[t]
        for i in range(1,n+1):
            rec(i,dp,0)
        return dp[-1]