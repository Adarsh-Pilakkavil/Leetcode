class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost)+1)
        a=cost[0]
        b=cost[1]
        if len(cost)==2:
            return min(cost)
        for i in range(2,len(cost)):
            c=min(a,b)+cost[i]
            a=b
            b=c
        dp[-1]=min(a,b)
        return dp[-1]