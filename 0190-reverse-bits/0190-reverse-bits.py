class Solution:
    def reverseBits(self, n: int) -> int:
        
        y=("0"*(34-len(bin(n)))+bin(n)[2:])[::-1]
        k=0
        n=31
        for i in y:
            k+=int(i)*(2**n)
            n-=1
        return k