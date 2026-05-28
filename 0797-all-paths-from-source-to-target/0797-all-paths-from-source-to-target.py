class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n=len(graph)
        ans=[]
        def dfs(i,graph,l):
            l.append(i)
            if i==n-1:
                ans.append(l[:])
                return
            for k in graph[i]:
                dfs(k,graph,l[:])
        dfs(0,graph,[])
        return ans