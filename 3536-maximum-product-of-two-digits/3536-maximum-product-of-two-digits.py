class Solution:
    def maxProduct(self, n: int) -> int:
        a=max(n%10,(n//10)%10)
        b=min(n%10,(n//10)%10)
        n=n//100
        while n:
            d=n%10
            n=n//10
            if a<=d:
                a,b=d,a
            elif a>d>b:
                b=d
            else:
                continue
        return a*b
