class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        c=0
        for i in range(len(nums)//2):
            c=max(c,nums[i]+nums[len(nums)-1-i])
        return c