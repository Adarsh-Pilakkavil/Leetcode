class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s=sorted(nums)
        d={}
        for i,v in enumerate(s):
            if v not in d:
                d[v] = i
        return [d[x] for x in nums]