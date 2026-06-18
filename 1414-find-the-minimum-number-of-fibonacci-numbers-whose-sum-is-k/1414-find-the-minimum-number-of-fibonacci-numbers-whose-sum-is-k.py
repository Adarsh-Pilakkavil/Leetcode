class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        l=[]
        a=1
        b=1
        c=0
        l.append(a)
        while b<=k:
            l.append(b)
            a,b=b,a+b
        l=l[::-1]
        for i in l:
            if k<i:
                continue
            elif k==i:
                return c+1
            else:
                k-=i
                c+=1
        return c