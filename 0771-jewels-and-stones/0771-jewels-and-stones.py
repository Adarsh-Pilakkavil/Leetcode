class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        z=0
        for i in jewels:
            for j in stones:
                if i==j:
                    z+=1
        return z