class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums[0]<nums[1]:
            a,b=nums[1],nums[0]
        else:
            b,a=nums[1],nums[0]
        for i in range(2,len(nums)):
            if nums[i]>=a:
                b=a
                a=nums[i]
            elif a>nums[i]>b:
                b=nums[i]
            else:
                continue
        print(a,b)
        return (a-1)*(b-1)