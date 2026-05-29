class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1=[0]*(len(nums)-1)
        dp2=[0]*(len(nums)-1)       
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums)
        dp1[0]=nums[0]
        dp1[1]=max(nums[0],nums[1])
        dp2[0]=nums[1]
        dp2[1]=max(nums[1],nums[2])
        for i in range(2,len(nums)-1):
            in1=dp1[i-2]+nums[i]
            in2=dp2[i-2]+nums[i+1]
            out1=dp1[i-1]
            out2=dp2[i-1]
            dp1[i]=max(in1,out1)
            dp2[i]=max(in2,out2)
        return max(dp1[-1],dp2[-1])