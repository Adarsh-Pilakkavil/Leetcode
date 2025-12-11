class Solution(object):
    def prefixCount(self, words, pref):
        count=0
        for j in words:
            if j[0:len(pref):1]==pref:
                count+=1
        return count