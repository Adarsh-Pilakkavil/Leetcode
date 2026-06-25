class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        c=0
        for i in range(len(nums)):
            t=0
            for j in range(i,len(nums)):
                if nums[j]==target:
                    t+=1
                l=j-i+1
                if t>l//2:
                    c+=1
        return c