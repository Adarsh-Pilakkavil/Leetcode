class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s=list(str(n))
        s=[int(x) for x in s]
        sum=0
        for i in range(len(s)):
            if i%2==0:
                sum+=s[i]
            else:
                sum-=s[i]
        return sum