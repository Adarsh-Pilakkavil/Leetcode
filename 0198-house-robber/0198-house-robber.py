class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            #in take
            in_take=dp[i-2]+nums[i]
            out_take=dp[i-1]
            dp[i]=max(in_take,out_take)
        return dp[len(nums)-1]