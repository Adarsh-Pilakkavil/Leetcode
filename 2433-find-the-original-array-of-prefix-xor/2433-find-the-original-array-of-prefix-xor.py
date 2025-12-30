class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        k=0
        l=[]
        for i in range(0,len(pref)):
            l.append(k^pref[i])
            k=k^l[-1]
        return l