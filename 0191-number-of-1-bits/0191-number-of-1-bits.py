class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        def co(n):
            nonlocal count
            if n==1:
                return count+1
            if n%2==1:
                count+=1
            return co(n//2)
        return co(n)
        