class Solution(object):
    def removeDuplicates(self, nums):
        count=0
        r=0
        for i in range(len(nums)):
            if nums[i]==nums[r]:
                continue
            else:
                r+=1
                nums[r]=nums[i]
        return r+1


        