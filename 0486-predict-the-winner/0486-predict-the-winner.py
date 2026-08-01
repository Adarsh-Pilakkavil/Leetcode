class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if ~len(nums) & 1:
            return True
        def rec(i,j):
            if i==j:
                return nums[i]
            return max(nums[i]-rec(i+1,j),nums[j]-rec(i,j-1))
        return rec(0,len(nums)-1)>=0