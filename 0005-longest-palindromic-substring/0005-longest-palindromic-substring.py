class Solution:
    def longestPalindrome(self, s: str) -> str:
        i=0
        j=len(s)-1
        dp=[]
        if len(s)==1:
            return s
        for i in range(len(s)):
            dp.append([0]*len(s))
        def rec(i,j,dp):
            if i>j:
                return ""
            if i==j:
                return s[i]
            if dp[i][j]:
                return dp[i][j]
            if s[i:j+1]==s[i:j+1][::-1]:
                dp[i][j]=s[i:j+1]
            else:
                if len(rec(i+1,j,dp))>len(rec(i,j-1,dp)):
                    dp[i][j]=rec(i+1,j,dp)
                else:
                    dp[i][j]=rec(i,j-1,dp)
            return dp[i][j]
        return rec(0,len(s)-1,dp)