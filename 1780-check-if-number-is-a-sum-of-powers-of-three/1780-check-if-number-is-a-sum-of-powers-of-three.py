class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        i=-1
        while n>=(3**(i+1)):
            i+=1
        while i>=0:
            if n>=3**i:
                n-=3**i
            i-=1
        return n==0