class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        k=n
        while n:
            d=n%10
            n=n//10
            s+=d
            p*=d
        return k%(s+p)==0