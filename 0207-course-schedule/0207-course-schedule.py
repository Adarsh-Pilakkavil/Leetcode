from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList=[]
        q=deque()
        ans=[]
        for i in range(numCourses):
            adjList.append([])
        indegree=[0]*numCourses
        for i in prerequisites:
            indegree[i[0]]+=1
            adjList[i[1]].append(i[0])
        for i in range(numCourses):
            if indegree[i]==0:
                ans.append(i)
                q.append(i)
        while q:
            n=q.popleft()
            for i in adjList[n]:
                indegree[i]-=1
                if indegree[i]==0:
                    ans.append(i)
                    q.append(i)
        return len(ans)==numCourses