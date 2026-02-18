class Solution:
    def findComplement(self, num: int) -> int:
        k=0
        t=0
        while num!=0:
            k+=(1-num%2)*(2**t)
            t+=1
            num=num//2
        return k