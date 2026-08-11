class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prev=nums[0]
        s=nums[0]
        ans=0
        for i in range(1,len(nums)):
            if nums[i]==prev+1:
                s+=nums[i]
                prev=nums[i]
            else:
                ans=max(ans,s)
                break
        ans=max(ans,s)
        while True:
            if ans in nums:
                ans+=1
                continue
            else:
                return ans
        return ans