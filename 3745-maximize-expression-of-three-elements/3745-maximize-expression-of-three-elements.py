class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        a=max(nums)
        c=min(nums)
        b=nums.index(a)
        b=max(nums[:b]+nums[b+1:])
        return a+b-c