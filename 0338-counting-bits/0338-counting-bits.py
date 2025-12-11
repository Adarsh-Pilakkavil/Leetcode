class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(0,n+1,1):
            count=0
            y=bin(i)[2:]
            for j in y:
                if j=='1':
                    count+=1
            l.append(count)
        return l