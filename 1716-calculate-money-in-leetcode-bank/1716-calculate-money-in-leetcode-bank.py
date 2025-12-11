class Solution:
    def totalMoney(self, n: int) -> int:
        c=0
        tot=0
        while n>0:
            if n<7:
                tot+=(n*(n+1))//2+c*n
                break
            else:
                tot+=c*7+28
                c+=1
                n-=7
        return tot