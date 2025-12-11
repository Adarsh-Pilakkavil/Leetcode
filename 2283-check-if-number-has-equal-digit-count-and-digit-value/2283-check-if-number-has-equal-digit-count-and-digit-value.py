class Solution:
    def digitCount(self, num: str) -> bool:
        l=list(num)
        l=[int(x) for x in l]
        for i in range(len(l)):
            if l.count(i)!=l[i]:
                return False
        return True