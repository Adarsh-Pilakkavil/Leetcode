class Solution(object):
    def truncateSentence(self, s, k):
        count=0
        st=''
        for i in s:
            if i==" ":
                count+=1
            if count==k:
                return st
            st+=i
        return st
        