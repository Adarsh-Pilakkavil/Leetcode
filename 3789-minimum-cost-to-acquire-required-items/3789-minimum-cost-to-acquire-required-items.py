class Solution(object):
    def minimumCost(self, cost1, cost2, costboth, need1, need2):
        """
        :type cost1: int
        :type cost2: int
        :type costBoth: int
        :type need1: int
        :type need2: int
        :rtype: int
        """
        s=0
        n=min(need1,need2)
        if costboth<cost1+cost2:
            s+=n*costboth
            if n==need1:
                if costboth<cost2:
                    return s+(need2-n)*costboth
                else:
                    return s+(need2-n)*cost2
            else:
                if costboth<cost1:
                    return s+(need1-n)*costboth
                else:
                    return s+(need1-n)*cost1
        else:
            return cost1*need1+cost2*need2