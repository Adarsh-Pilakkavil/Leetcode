class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mi=min(nums)
        ma=max(nums)
        l=[]
        for i in range(mi,ma+1,1):
            if i not in nums:
                l.append(i)
        return l