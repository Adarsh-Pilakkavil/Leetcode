class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c=0
        def rec(i,s,fin):
            nonlocal c
            if i==len(s):
                c=max(c,len(fin))
                return
            if s[i] in fin:
                c=max(c,len(fin))
            else:
                fin+=s[i]
                rec(i+1,s,fin)
            return c
        for i in range(len(s)):
            rec(i,s,"")
        return c