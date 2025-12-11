class Solution:
    def minOperations(self, nums: List[int]) -> int:
        t=0
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                continue
            else:
                t+=nums[i]-nums[i+1]+1
                nums[i+1]=nums[i]+1
        return t