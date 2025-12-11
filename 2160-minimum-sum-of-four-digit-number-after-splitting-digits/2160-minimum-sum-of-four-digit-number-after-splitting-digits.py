class Solution:
    def minimumSum(self, num: int) -> int:
        l=list(str(num))
        l.sort()
        n1=int(l[0])*10+int(l[3])
        n2=int(l[1])*10+int(l[2])
        return n1+n2