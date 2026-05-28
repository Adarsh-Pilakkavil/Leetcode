class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[False]*len(rooms)
        visited[0]=True
        def dfs(i,visited,rooms):
            for j in rooms[i]:
                if not visited[j]:
                    visited[j]=True
                    dfs(j,visited,rooms)
        dfs(0,visited,rooms)
        return visited==[True]*len(rooms)