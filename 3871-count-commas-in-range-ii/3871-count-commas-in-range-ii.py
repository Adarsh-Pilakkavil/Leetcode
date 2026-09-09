class Solution:
    def countCommas(self, n: int) -> int:
        c=0
        i=0
        k=1
        while n>=(10**(i+3)):
            if n>=(10**(i+6)):
                c+=k*(10**(i+6)-10**(i+3))
            else:
                c+=k*(n-10**(i+3)+1)
            i+=3
            k+=1
        return c