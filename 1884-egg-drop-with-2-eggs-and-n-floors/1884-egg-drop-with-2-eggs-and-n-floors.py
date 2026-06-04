class Solution:
    def twoEggDrop(self, n: int) -> int:
        c=0
        while n>0:
            n-=c
            c+=1
        c-=1
        return c