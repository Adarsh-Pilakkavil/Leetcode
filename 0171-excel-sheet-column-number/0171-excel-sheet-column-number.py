class Solution(object):
    def titleToNumber(self, columnTitle):
        k=0
        for i in range(0,len(columnTitle),1):
            k+=(ord(columnTitle[i])-64)*(26**(len(columnTitle)-1-i))
        return k