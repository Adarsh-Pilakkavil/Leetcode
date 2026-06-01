class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        total=sum(nums)
        if len(nums)==1:
            return False
        if sum(nums)%2==1:
            return False
        dp=[[-1 for j in range(total//2+1)] for i in range(n)]
        def rec(i,sum1,nums,total):
            if sum1>total//2:
                return False
            elif sum1==total//2:
                return True
            elif i==len(nums):
                return False
            if dp[i][sum1]!=-1:
                return dp[i][sum1]
            t=rec(i+1,sum1+nums[i],nums,total)
            nt=rec(i+1,sum1,nums,total)
            dp[i][sum1]=t or nt
            return dp[i][sum1]
        return rec(0,0,nums,sum(nums))
