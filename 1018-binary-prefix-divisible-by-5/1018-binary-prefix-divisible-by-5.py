class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        l=[]
        value=0
        for i in nums:
            value= (2*value+i)%5
            if value==0:
                l.append(True)
            else:
                l.append(False)
        return l