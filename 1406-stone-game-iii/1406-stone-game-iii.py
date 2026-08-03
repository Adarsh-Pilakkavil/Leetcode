class Solution:
    def stoneGameIII(self, v: List[int]) -> str:
        dp=[None]*(len(v))
        def rec(dp,i):
            if i==len(v):
                return 0
            if dp[i] is not None:
                return dp[i]
            m=float("-inf")
            curr=0
            for t in range(1,4):
                if i+t<=len(v):
                    curr+=v[i+t-1]
                    m=max(m,curr-rec(dp,i+t))
            dp[i]=m
            return dp[i]
        k=rec(dp,0)
        if k>0:
            return "Alice"
        elif k<0:
            return "Bob"
        else:
            return "Tie"
