class Solution:
    def smallestNumber(self, n: int) -> int:
        k=len(bin(n)[2:])
        return int("1"*k,2)