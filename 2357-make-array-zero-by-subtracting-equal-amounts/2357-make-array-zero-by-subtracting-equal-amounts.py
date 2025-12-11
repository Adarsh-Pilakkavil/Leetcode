class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums=list(set(nums))
        nums.sort()
        c=0
        for i in nums:
            if i<=0:
                continue
            else:
                c+=1
        return c