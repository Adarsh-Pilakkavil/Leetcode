class Solution:
    def smallestPalindrome(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        t="abcdefghijklmnopqrstuvwxyz"
        c=""
        pivot=""
        for i in t:
            if i in d:
                c+=i*(d[i]//2)
                if d[i]%2==1:
                    pivot=i
        return c+pivot+c[::-1]