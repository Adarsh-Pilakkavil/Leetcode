class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        s2=[]
        for i in s:
            if s1 and i=="#":
                s1.pop()
            else:
                if i=="#":
                    continue
                s1.append(i)
        for i in t:
            if s2 and i=="#":
                s2.pop()
            else:
                if i=="#":
                    continue
                s2.append(i)
        return s1==s2