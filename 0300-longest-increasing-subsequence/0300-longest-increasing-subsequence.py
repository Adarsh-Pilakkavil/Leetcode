class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[[-1 for i in range(len(nums))]for j in range(len(nums))]
        def rec(i,prev,nums,dp):
            if i==len(nums):
                return 0
            take=0
            if dp[i][prev]!=-1:
                return dp[i][prev]
            if prev==-1 or nums[prev]<nums[i]:
                take=1+rec(i+1,i,nums,dp)
            not_take=rec(i+1,prev,nums,dp)
            dp[i][prev]=max(take,not_take)
            return dp[i][prev]
        return rec(0,-1,nums,dp)