class Solution:
    def maxDistinct(self, s: str) -> int:
        l=[]
        c=0
        for i in s:
            if i in l:
                continue
            else:
                c+=1
                l.append(i)
        return c