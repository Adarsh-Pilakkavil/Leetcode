class Solution(object):
    def climbStairs(self, n):
        a1=1
        a2=2
        t=0
        if n==1:
            return a1
        if n==2:
            return a2
        for i in range(0,n-2,1):
            t=a1+a2
            a1=a2
            a2=t
        return a2