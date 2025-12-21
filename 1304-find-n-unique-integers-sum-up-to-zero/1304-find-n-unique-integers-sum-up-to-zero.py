class Solution:
    def sumZero(self, n: int) -> List[int]:
        l=[]
        if n%2==1:
            for i in range(0,n//2+1):
                if i==0:
                    l.append(i)
                    continue
                l.append(i)
                l.append(-i)
            return l
        else:
            for i in range(1,n//2+1):
                l.append(i)
                l.append(-i)
            return l