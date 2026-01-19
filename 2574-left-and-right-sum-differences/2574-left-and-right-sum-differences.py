class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        k=sum(nums)
        l=[]
        s=0
        for i in nums:
            l.append(abs(k-i-2*s))
            s+=i
        return l