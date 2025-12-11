class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target-nums[i] in nums:
                k=nums.index(target-nums[i])
                if i==k:
                    continue
                if i<k:
                    return [i,k]
                else:
                    return [k,i]
        