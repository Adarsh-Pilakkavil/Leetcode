class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        start=0
        ans=0
        d={}
        for i in range(len(s)):
            if s[i] in d and d[s[i]]>=2:
                d[s[i]]+=1
                ans=max(ans,i-start)
                while d[s[i]]>2:
                    d[s[start]]-=1
                    start+=1
            else:
                d[s[i]]=d.get(s[i],0)+1
            print(ans)
        ans=max(ans,i-start+1)
        return ans