class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def su(num):
            summ=0
            while num!=0:
                d=num%10
                summ+=d
                num=num//10
            return summ
        l=''
        for ki in s:
            l+=str(ord(ki)-96)
        l=int(l)
        while k!=0:
            l=su(l)
            k-=1
        return l