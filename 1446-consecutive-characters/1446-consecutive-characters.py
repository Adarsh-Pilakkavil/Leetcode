class Solution:
    def maxPower(self, s: str) -> int:
        curr=s[0]
        count=0
        maxx=0
        for i in s:
            if curr==i:
                count+=1
            if count>=maxx:
                maxx=count
            if curr!=i:
                count=1
                curr=i
        return maxx