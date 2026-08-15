class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n=len(nums)
        if [0]*n==nums:
            return 0
        x=0
        for i in nums:
            x=x^i
        if x:
            return n
        return n-1