class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList=[]
        indeg=[False]*n
        for i in range(n):
            adjList.append([])
        for i in edges:
            adjList[i[0]].append(i[1])
            indeg[i[1]]=True
        s=[]
        for i in range(len(indeg)):
            if not indeg[i]:
                s.append(i)
        return s