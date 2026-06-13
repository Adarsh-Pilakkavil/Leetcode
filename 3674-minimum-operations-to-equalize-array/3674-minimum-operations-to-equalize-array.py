class Solution:
    def minOperations(self, nums: List[int]) -> int:
        k=nums[0]
        for i in nums:
            if i!=k:
                return 1
        return 0