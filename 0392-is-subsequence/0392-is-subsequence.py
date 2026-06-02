class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i1,i2=0,0
        if s=="":
            return True
        if t=="":
            return False
        while i2!=len(t):
            if s[i1]==t[i2]:
                i1+=1
                i2+=1
            else:
                i2+=1
            if i1==len(s):
                return True
        return False