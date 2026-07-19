class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        def gcd(x,y):
            if y==0:
                return x
            x,y=y,x%y
            return gcd(x,y)
        if target>x+y:
            return False
        if target==0:
            return True
        k=gcd(max(x,y),min(x,y))
        return target%k==0