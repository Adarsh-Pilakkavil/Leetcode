class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        d={}
        for i in nums:
            d[i]=1
        c=k
        while True:
            if c in d:
                c+=k
            else:
                return c