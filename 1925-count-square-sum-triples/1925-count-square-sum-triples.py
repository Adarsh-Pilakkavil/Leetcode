class Solution:
    def countTriples(self, n: int) -> int:
        c=0
        for i in range(1,n+1,1):
            for j in range(1,n+1,1):
                k=i**2+j**2
                if int(k**0.5)**2==k and k**0.5<=n:
                    c+=1
        return c