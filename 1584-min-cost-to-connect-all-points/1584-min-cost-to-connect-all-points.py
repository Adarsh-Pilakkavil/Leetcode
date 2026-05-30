import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited=set()
        total=0
        heap=[(0,0)]
        while len(visited)<len(points):
            cost,node=heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            x1,y1=points[node]
            total+=cost
            for i in range(len(points)):
                if i not in visited:
                    x2,y2=points[i]
                    d=abs(x2-x1)+abs(y1-y2)
                    heappush(heap,(d,i))
        return total