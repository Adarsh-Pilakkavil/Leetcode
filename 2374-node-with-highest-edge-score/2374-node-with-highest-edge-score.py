class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        adjList=[0]*len(edges)
        for j in range(len(edges)):
            adjList[edges[j]]+=j
        return adjList.index(max(adjList))