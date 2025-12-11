class Solution(object):
    def numWaterBottles(self,numBottles, numExchange):
        def foo(a,num):
            t=a//num
            if t==0:
                return 0
            else:
                return t + foo(t+a%num,num)
        return numBottles + foo(numBottles,numExchange)
    
        