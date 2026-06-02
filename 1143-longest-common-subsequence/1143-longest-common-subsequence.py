class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[-1 for i in range(len(text2))] for j in range(len(text1))]
        def rec(i,j,text1,text2,dp):
            if i==len(text1) or j==len(text2):
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            dp[i][j]=0
            if text1[i]==text2[j]:
                dp[i][j]=1+rec(i+1,j+1,text1,text2,dp)
                return dp[i][j]
            dp[i][j]=max(rec(i+1,j,text1,text2,dp),rec(i,j+1,text1,text2,dp))
            return dp[i][j]
        return rec(0,0,text1,text2,dp)