class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        c=0
        for i in nums:
            if i%2==0:
                c+=1
            if c==2:
                return True
        return False