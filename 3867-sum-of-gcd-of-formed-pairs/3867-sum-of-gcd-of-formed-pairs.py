class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(m,n):
            if n==0:
                return m
            m,n=n,m%n
            return gcd(m,n)
        m=0
        l=[]
        for i in nums:
            if i>m:
                m=i
                l.append(i)
            else:
                l.append(gcd(m,i))
        l.sort()
        c=0
        for i in range(len(l)//2):
            c+=gcd(l[i],l[len(l)-1-i])
        return c