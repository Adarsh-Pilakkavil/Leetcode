class Solution(object):
    def maxFreqSum(self, s):
        v,c=0,0
        for i in s:
            if i in ["a","e","i","o","u"]:
                if s.count(i)>v:
                    v=s.count(i)
            else:
                if s.count(i)>c:
                    c=s.count(i)
        return v+c