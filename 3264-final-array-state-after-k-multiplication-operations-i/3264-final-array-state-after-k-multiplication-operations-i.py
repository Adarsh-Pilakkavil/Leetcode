class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        def foo(n):
            if n==0:
                return nums
            t=0
            mini=nums[0]
            for i in range(0,len(nums),1):
                if nums[i]<mini:
                    mini=nums[i]
                    t=i
            print(mini)
            nums[t]*=multiplier
            return foo(n-1)
        return foo(k)