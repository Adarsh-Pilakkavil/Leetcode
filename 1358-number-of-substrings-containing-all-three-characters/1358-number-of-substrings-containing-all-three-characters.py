class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n=len(s)
        ans=0
        l=0
        count=[0,0,0]
        for right in range(n):
            count[ord(s[right])-ord("a")]+=1
            while count[0] and count[1] and count[2]:
                ans+=n-right
                count[ord(s[l])-ord("a")]-=1
                l+=1
        return ans