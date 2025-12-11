class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        summ=0
        for i in nums:
            l=list(str(i))
            l=[int(x) for x in l]
            summ+=sum(l)
        return abs(sum(nums)-summ)