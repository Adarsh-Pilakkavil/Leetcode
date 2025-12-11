class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if len(nums)==1:
            if nums[0]==original:
                return original*2
        i=0
        for i in range(len(nums)):
            if nums[i]==original:
                original*=2
                i=-1
        return original