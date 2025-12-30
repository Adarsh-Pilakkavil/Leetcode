class Solution(object):
    def minAllOneMultiple(self, k):
        """
        :type k: int
        :rtype: int
        """
        if k%2==0 or k%5==0:
            return -1
        n=1
        remainder=1
        while remainder!=0:
            if remainder==0:
                return n
            remainder=(remainder*10+1)%k
            n+=1
        return n