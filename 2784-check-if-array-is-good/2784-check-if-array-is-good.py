class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums)!=max(nums)+1:
            return False
        x=set()
        for i in nums:
            if i==max(nums):
                x.add(i)
                continue
            if i in x:
                return False
            x.add(i)
        print(x)
        if nums.count(max(nums))==2:
            return True
        return False
                            