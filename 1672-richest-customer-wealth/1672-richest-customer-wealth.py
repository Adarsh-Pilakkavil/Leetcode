class Solution(object):
    def maximumWealth(self, accounts):
        k=0
        for i in accounts:
            if sum(i)>k:
                k=sum(i)
        return k
        