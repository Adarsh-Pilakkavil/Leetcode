class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[-1]*(len(word2)+1) for _ in range(len(word1)+1)]
        if word1==word2:
            return 0
        def rec(i,j):
            if j>=len(word2):
                return len(word1)-i
            if i>=len(word1):
                return len(word2)-j
            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i]==word2[j]:
                c=rec(i+1,j+1)
            else:
                c=min(1+rec(i+1,j+1),1+rec(i+1,j),1+rec(i,j+1))
            dp[i][j]=c
            return c
        return rec(0,0)