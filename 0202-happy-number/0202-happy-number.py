class Solution:
    def isHappy(self, n: int) -> bool:
        s=set()
        def f(x):
            sum=0
            while x>0:
                d=x%10
                sum+=d**2
                x=x//10
            if sum==1:
                return True
            if sum in s:
                return False
            s.add(sum)
            return f(sum)
        return f(n)
            