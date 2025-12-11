class Solution(object):
    def reverseDegree(self, s):
        sum=0
        k=1
        for i in s:
            sum+=(123-ord(i))*k
            k+=1
        return sum