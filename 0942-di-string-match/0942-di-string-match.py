class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i=0
        d=len(s)
        l=[]
        for k in s:
            if k=="I":
                l.append(i)
                i+=1
            else:
                l.append(d)
                d-=1
        return l+[d]