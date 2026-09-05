class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        t=k
        s=[0]*len(nums)
        s[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            s[i]=min(s[i+1],nums[i])
        k=float("-inf")
        for i in range(len(nums)):
            k=max(k,nums[i])
            if k-s[i]<=t:
                return i
        return -1
        