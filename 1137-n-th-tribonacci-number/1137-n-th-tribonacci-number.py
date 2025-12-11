class Solution(object):
    def tribonacci(self, n):
        a=0
        b,c=1,1
        i=3
        sum=0
        if n==1 or n==2:
            sum=1
        while(i<=n):
            sum=a+b+c
            a=b
            b=c
            c=sum
            i+=1
        return sum
        