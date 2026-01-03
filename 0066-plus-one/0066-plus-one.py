class Solution:
    def plusOne(self, l: List[int]) -> List[int]:
        k=len(l)-1
        while True:
            if k==-1:
                t=[1]
                t.extend(l)
                return t
            else:
                if l[k]==9:
                    l[k]=0
                    k-=1
                    continue
                else:
                    l[k]=l[k]+1
                    return l