class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ma=max(cost1,cost2)
        mi=min(cost2,cost1)
        k=total//ma
        count=0
        for i in range(0,k+1,1):
            c=total-(i*ma)
            count=count+c//mi+1
        return count
        