class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        d={}
        if k==len(nums):
            return max(nums)
        for i in nums:
            d[i]=d.get(i,0)+1
        a,b=nums[0],nums[-1]
        if k==1:
            m=-1
            for i in nums:
                if d[i]==1:
                    m=max(m,i)
            return m
        else:
            if d[a]>1 and d[b]>1:
                return -1
            elif d[a]>1:
                return b
            elif d[b]>1:
                return a
            else:
                return max(a,b)