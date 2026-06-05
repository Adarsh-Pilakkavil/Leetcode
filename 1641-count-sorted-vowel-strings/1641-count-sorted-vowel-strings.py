class Solution:
    def countVowelStrings(self, n: int) -> int:
        def bt(i,n):
            if n==0:
                return 1
            if i>=5:
                return 0
            t,nt=0,0
            t=bt(i,n-1)
            nt=bt(i+1,n)
            return t+nt
        return bt(0,n)
