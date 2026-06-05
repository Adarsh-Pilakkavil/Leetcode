class Solution:
    def countVowelStrings(self, n: int) -> int:
        def rec(n,lc):
            if n==0:
                return 1
            c=0
            for i in range(lc,5):
                c+=rec(n-1,i)
            return c
        return rec(n,0)
