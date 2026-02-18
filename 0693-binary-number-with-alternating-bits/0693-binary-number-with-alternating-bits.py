class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        t=-1
        while n!=0:
            d=n%2
            if t==d:
                return False
            if t==-1:
                t=d
            t=d
            n=n//2
        return True