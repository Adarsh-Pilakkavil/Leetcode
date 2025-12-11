class Solution(object):
    def singleNumber(self, nums):
        for i in range(0,len(nums),1):
            if nums.count(nums[i])!=2:
                return nums[i]
        