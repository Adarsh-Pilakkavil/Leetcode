class Solution(object):
    def countDistinctIntegers(self, nums):
        k=len(nums)
        for i in range(0,k,1):
            nums.append(int(str(nums[i])[::-1]))
        return len(set(nums))
        