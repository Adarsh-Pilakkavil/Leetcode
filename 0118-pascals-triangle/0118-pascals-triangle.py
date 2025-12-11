class Solution(object):
    def generate(self, numRows):
        l=[[1]]
        k=[]
        for i in range(0,numRows,1):
            if i==0:
                continue
            if i==1:
                l.append([1,1])
                continue
            for j in range(0,i+1,1):
                if j==0 or j==i:
                    k.append(1)
                    continue
                k.append(l[i-1][j]+l[i-1][j-1])
            l.append(k)
            k=[]
        return l
                
        