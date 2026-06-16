class Solution:
    def processStr(self, s: str) -> str:
        t=""
        for i in s:
            if i=="*":
                if t:
                    t=t[:len(t)-1]
            elif i=="#":
                t+=t
            elif i=="%":
                t=t[::-1]
            else:
                t+=i
        return t