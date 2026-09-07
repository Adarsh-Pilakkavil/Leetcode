class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp=[0]*len(s)
        dp[0]=1
        d={}
        d[s[0]]=0
        for i in range(1,len(s)):
            if s[i] in d:
                dp[i]=dp[i-1]*2-dp[d[s[i]]-1]
                d[s[i]]=i
            else:
                d[s[i]]=i
                dp[i]=2*dp[i-1]+1
        return dp[-1]%(10**9+7)