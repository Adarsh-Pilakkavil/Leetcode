class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        l=[]
        for i in image:
            k=i[::-1]
            for j in range(len(k)):
                if k[j]==1:
                    k[j]=0
                else:
                    k[j]=1
            l.append(k)
        return l