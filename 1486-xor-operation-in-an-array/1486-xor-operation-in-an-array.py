class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        k=start
        for i in range(2,2*n,2):
            k=k^(start+i)
        return k

        