class Solution:
    def countAsterisks(self, s: str) -> int:
        f=True
        c=0
        i=0
        while i!=len(s):
            if s[i]=="|":
                f=not f
                i+=1
            else:
                if f and s[i]=="*":
                    c+=1
                    i+=1
                else:
                    i+=1
        return c