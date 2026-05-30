class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=[False]*n
        adjList=[]
        for i in range(n):
            adjList.append([])
        for i in edges:
            adjList[i[0]].append(i[1])
            adjList[i[1]].append(i[0])
        def dfs(i):
            visited[i]=True
            v_count=1
            e_count=len(adjList[i])
            for j in adjList[i]:
                if not visited[j]:
                    nv,ne=dfs(j)
                    v_count+=nv
                    e_count+=ne
            return v_count,e_count
        c=0
        for i in range(n):
            if not visited[i]:
                vert,edge=dfs(i)
                if edge==vert*(vert-1):
                    c+=1
        return c