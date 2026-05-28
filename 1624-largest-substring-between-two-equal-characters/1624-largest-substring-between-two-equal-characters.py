class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d={}
        c=-1
        for i in range(len(s)):
            if s[i] in d:
                c=max(c,i-d[s[i]]-1)
            else:
                d[s[i]]=i
        return c