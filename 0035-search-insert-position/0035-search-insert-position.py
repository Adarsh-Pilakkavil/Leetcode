class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(0,len(nums),1):
            if nums[i]>=target:
                return i
        return len(nums)
        