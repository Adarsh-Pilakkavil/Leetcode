class Solution:
    def minOperations(self, nums: List[int]) -> int:
        i=0
        c=0
        while i!=len(nums):
            if i>=len(nums)-2 and nums[i]==0:
                return -1
            if nums[i]==0:
                nums[i]=1
                nums[i+1]=1 if nums[i+1]==0 else 0
                nums[i+2]=1 if nums[i+2]==0 else 0
                c+=1
            i+=1
        return c
