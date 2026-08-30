class Solution:
    def validPalindrome(self, s: str) -> bool:
        def rec(i,j,k):
            if i>len(s)//2:
                return True
            if s[i]==s[j]:
                return rec(i+1,j-1,k)
            else:
                if k==0:
                    return False
                else:
                    return rec(i+1,j,0) or rec(i,j-1,0)
        return rec(0,len(s)-1,1)