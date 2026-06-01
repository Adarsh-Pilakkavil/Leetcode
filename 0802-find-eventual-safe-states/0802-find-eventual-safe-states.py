class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        adjList=graph
        vis=[0]*n
        def dfs(i):
            if vis[i]==1:
                return True
            if vis[i]==2:
                return False
            vis[i]=1
            for j in graph[i]:
                if dfs(j):
                    return True
            vis[i]=2
            return False
        l=[]
        for i in range(n):
            if not dfs(i):
                l.append(i)   
        return l         