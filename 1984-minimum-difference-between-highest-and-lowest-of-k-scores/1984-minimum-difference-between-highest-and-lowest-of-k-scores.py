class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        t=10**10
        for i in range(len(nums)-k+1):
            t=min(t,nums[i+k-1]-nums[i])
        if t==10**10:
            return 0
        return t