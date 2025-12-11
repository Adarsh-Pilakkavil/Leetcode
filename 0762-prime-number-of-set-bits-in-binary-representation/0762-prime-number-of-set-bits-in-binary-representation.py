class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count=0
        def pri(n):
            if n==1 or n==0:
                return False
            for i in range(2,n,1):
                if n%i==0:
                    return False
            return True
        for i in range(left,right+1,1):
            if pri(bin(i)[2:].count("1")):
                count+=1
        return count