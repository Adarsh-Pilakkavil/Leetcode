class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        t=sum(nums)
        if n==1:
            return False
        if t%2==1:
            return False
        t=t//2
        dp=[False]*(t+1)
        dp[0]=True
        for num in nums:
            for i in range(t,num-1,-1):
                if dp[i-num]:
                    dp[i]=True
        return dp[-1]
                