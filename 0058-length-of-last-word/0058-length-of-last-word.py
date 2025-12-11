class Solution(object):
    def lengthOfLastWord(self, s):
        s1=s.rstrip()
        k=0
        for i in range(len(s1)-1,-1,-1):
            if s1[i]==" ":
                break
            k+=1
        return k
        