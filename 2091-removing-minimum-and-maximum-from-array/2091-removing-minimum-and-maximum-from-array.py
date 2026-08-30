class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        k1=nums.index(max(nums))
        k2=nums.index(min(nums))
        l=max(k1+1,k2+1)
        r=max(len(nums)-k1,len(nums)-k2)
        t=min(k1+1+len(nums)-k2,k2+1+len(nums)-k1)
        print(l,r,t)
        return min(l,r,t)