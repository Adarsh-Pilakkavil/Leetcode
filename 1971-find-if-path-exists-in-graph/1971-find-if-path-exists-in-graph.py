from collections import deque
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjl=[]
        for i in range(n):
            adjl.append([])
        for edge in edges:
            x=edge[0]
            y=edge[1]
            adjl[x].append(y)
            adjl[y].append(x)
        q=deque()
        q.append(source)
        visited=[False]*n
        while q:
            n=q.popleft()
            for i in adjl[n]:
                if not visited[i]:
                    visited[i]=True
                    q.append(i)
            if visited[destination] or source==destination:
                return True
        return False