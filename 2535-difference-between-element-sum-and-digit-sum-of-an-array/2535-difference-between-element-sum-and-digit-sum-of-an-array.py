class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ans= 0
        for i in nums:
            ans+= i
            while i:
                ans-=i%10
                i//=10
        return ans