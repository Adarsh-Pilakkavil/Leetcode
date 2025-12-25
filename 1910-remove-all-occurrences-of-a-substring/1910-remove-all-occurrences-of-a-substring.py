class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        p=len(part)
        i=0
        if len(s)-p+1<0:
            return s
        while i<len(s)-p+1:
            if s[i:i+p]==part:
                s=s[:i]+s[i+p:]
                i=0
            else:
                i+=1
        return s