class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        d=[]
        for i in range(len(s)-1):
            d.append(s[i]+s[i+1])
        s=s[::-1]
        for i in range(len(s)-1):
            if d[i] in s:
                return True
        return False
