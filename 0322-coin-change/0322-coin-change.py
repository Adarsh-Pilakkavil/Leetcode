class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp={}
        def rec(coins,amount,dp):
            if amount==0:
                return 0
            if amount<0:
                return float("inf")
            mincoin=float("inf")
            if amount in dp:
                return dp[amount]
            for r in coins:
                res=rec(coins,amount-r,dp)
                if res!=float("inf"):
                    mincoin=min(mincoin,res+1)
            dp[amount]=mincoin
            return mincoin
        result=rec(coins,amount,dp)
        return result if result!=float("inf") else -1