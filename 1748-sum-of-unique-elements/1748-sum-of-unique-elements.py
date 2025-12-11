class Solution(object):
    def sumOfUnique(self, nums):
        a=0
        for i in nums:
            if nums.count(i)==1:
                a+=i
        return a
        