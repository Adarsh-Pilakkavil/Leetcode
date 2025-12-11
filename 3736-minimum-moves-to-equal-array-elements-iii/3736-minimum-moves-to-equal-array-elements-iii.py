class Solution:
    def minMoves(self, nums: List[int]) -> int:
        k=max(nums)
        sum=0
        for i in nums:
            sum+=k-i
        return sum