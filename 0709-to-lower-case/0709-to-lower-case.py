class Solution(object):
    def toLowerCase(self, s):
        st=""
        for a in s:
            if ord(a)>=65 and ord(a)<=90:
                st+=chr(ord(a)+32)
            else:
                st+=a
        return st