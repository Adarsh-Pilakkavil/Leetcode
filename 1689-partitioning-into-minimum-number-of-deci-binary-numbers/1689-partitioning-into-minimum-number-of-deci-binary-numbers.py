class Solution(object):
    def minPartitions(self, n):
        k=0
        for i in n: 
            if i>k:
               k=i
        return int(k)
        