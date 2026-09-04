class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        t=k
        k=nums[-1]
        mi=[k]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<k:
                k=nums[i]
            mi=[k]+mi
        k=nums[0]
        ma=[k]
        for i in range(1,len(nums)):
            if nums[i]>k:
                k=nums[i]
            ma.append(k)
        res=[]
        print(ma,mi)
        for j in range(len(nums)):
            if (ma[j]-mi[j])<=t:
                return j
        return -1