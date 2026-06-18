class Solution:
    def romanToInt(self, s: str) -> int:
        prev=0
        ans=0
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for i in range(len(s)-1,-1,-1):
            if d[s[i]]<prev:
                ans-=d[s[i]]
            else:
                ans+=d[s[i]]
            prev=d[s[i]]
        return ans