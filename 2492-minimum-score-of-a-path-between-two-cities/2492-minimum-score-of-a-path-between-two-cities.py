from collections import deque
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adjmatrix=[[] for i in range(n)]
        for i in roads:
            adjmatrix[i[0]-1].append((i[1]-1,i[2]))
            adjmatrix[i[1]-1].append((i[0]-1,i[2]))
        q=deque()
        q.append(0)
        visited=[0 for i in range(n)]
        visited[0]=1
        m=float("inf")
        while q:
            t=q.popleft()
            for i in adjmatrix[t]:
                m=min(m,i[1])
                if not visited[i[0]]:
                    visited[i[0]]=1
                    q.append(i[0])
        return m