class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ans=[0]*(len(edges)+1)
        for i in edges:
            ans[i[0]-1]+=1
            ans[i[1]-1]+=1
        ma=0
        ind=0
        print(ans)
        for i in range(len(ans)):
            if ans[i]>ma:
                ma=ans[i]
                ind=i+1
        return ind
