class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        l=[]
        if n==1:
            return 1
        if n==2:
            return 2
        i=1
        while 2**(i)<=n:
            i+=1
        return 2**i
