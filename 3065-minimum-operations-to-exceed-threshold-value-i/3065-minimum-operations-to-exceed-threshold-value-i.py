class Solution(object):
    def minOperations(self, nums, k):
        j=0
        for i in nums:
            if i<k:
                j+=1
        return j