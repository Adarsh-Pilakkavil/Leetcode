class Solution(object):
    def transformArray(self, nums):
        l=[]
        for i in nums:
            if i%2==0:
                l+=[0]
            else:
                l+=[1]
        return sorted(l)