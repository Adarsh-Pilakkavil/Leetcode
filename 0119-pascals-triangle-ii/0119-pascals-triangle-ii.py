class Solution(object):
    def getRow(self, rowIndex):
        
        for i in range(rowIndex+1):
            l=[1]*(i+1)
            for j in range(1,i,1):
                l[j]=k[j]+k[j-1]
            k=l
            if i==rowIndex:
                return  k