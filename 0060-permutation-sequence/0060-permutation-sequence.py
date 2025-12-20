import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k-=1
        s=[str(x) for x in range(1,n+1)]
        l=[]
        for i in range(n,0,-1):
            fa=math.factorial(i-1)
            ind=k//fa
            l.append(s.pop(ind))
            k=k%fa
        return "".join(l)