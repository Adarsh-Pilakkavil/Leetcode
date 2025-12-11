class Solution:
    def splitNum(self, num: int) -> int:
        l=sorted(list(str(num)))
        n1,n2="",""
        for i in range(0,len(l),1):
            if i%2==0:
                n1+=l[i]
            else:
                n2+=l[i]
        return int(n1)+int(n2)