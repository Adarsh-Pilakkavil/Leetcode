class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        s=[]
        result=[-1]*len(nums)
        for i,num in enumerate(nums):
            while s and num>nums[s[-1]]:
                li=s.pop()
                result[li]=num
            s.append(i)
        for i,num in enumerate(nums):
            while s and num>nums[s[-1]]:
                li=s.pop()
                result[li]=num
        return result