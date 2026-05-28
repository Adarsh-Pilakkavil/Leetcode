class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adjList=[]
        indeg=[0]*n
        for i in range(n):
            adjList.append([])
        for i in trust:
            adjList[i[1]-1].append(i[0]-1)
            indeg[i[0]-1]+=1
        for i in range(n):
            if indeg[i]==0 and len(adjList[i])==n-1:
                return i+1
        return -1