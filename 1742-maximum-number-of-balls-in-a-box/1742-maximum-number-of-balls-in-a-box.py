class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        d={}
        for i in range(lowLimit,highLimit+1,1):
            s=0
            x=i
            while x>0:
                s+=x%10
                x=x//10
            if s in d.keys():
                d[s]+=1
            else:
                d[s]=1
        return max(d.values())
