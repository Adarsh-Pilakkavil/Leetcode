class Solution(object):
    def reverse(self, x):
        if x<-(2**31) or x>((2**31)-1):
            return 0
        if x<0:
            y=-x
        else:
            y=x
        t=''
        while y>0:
            d=y%10
            t+=str(d)
            y=y//10
        if  t=='' or int(t)<-(2**31) or int(t)>((2**31)-1):
            return 0
        if x<0:
            return -int(t)
        return int(t)
        