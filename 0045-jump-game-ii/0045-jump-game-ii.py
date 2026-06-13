class Solution:
    def jump(self, nums: List[int]) -> int:
        dp=[-1]*len(nums)
        def rec(i,dp,nums):
            if i>=len(nums)-1:
                return 0
            if dp[i]!=-1:
                return dp[i]
            minj=float("inf")
            for j in range(1,nums[i]+1):
                minj=min(minj,1+rec(i+j,dp,nums))
            dp[i]=minj
            return dp[i]
        return rec(0,dp,nums)