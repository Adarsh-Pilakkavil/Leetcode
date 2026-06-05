class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[-1]*2 for j in range(len(prices))]
        def bt(i,dp,t):
            if i==len(prices):
                return 0
            if dp[i][t]!=-1:
                return dp[i][t]
            if t==0:
                buy=-prices[i]+bt(i+1,dp,1)
                skip=bt(i+1,dp,0)
                dp[i][t]=max(buy,skip)
            else:
                sell=prices[i]+bt(i+1,dp,0)
                skip=bt(i+1,dp,1)
                dp[i][t]=max(sell,skip)
            return dp[i][t]
        return bt(0,dp,0)