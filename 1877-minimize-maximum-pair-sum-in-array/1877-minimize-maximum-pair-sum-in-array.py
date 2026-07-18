class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        c=0
        n=len(nums)
        for i in range(n//2):
            c=max(c,nums[i]+nums[n-1-i])
        return c