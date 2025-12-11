class Solution:
    def minElement(self, nums: List[int]) -> int:
        def add(n):
            summ=0
            while n!=0:
                d=n%10
                n=n//10
                summ+=d
            return summ
        for i in range(0,len(nums),1):
            nums[i]=add(nums[i])
        return min(nums)
            