class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        visited=[False]*n
        adjList=[]
        for i in range(n):
            adjList.append([])
        for i in edges:
            adjList[i[0]].append(i[1])
            adjList[i[1]].append(i[0])
        def dfs(i,visited,adjList):
            visited[i]=True
            s=1
            for j in adjList[i]:
                if not visited[j]:
                    s+=dfs(j,visited,adjList)
            return s
        c=[]
        for i in range(n):
            if not visited[i]:
                c.append(dfs(i,visited,adjList))
        r=n
        a=0
        for i in c:
            r-=i
            a+=r*i
        return a