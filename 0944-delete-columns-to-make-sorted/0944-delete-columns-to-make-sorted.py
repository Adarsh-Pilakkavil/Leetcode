class Solution:
    def minDeletionSize(self, grid: List[str]) -> int:
        c=0
        for i in range(len(grid[0])):
            l=[]
            for j in range(len(grid)):
                if l==[] or ord(l[-1])<=ord(grid[j][i]):
                    l.append(grid[j][i])
                else:
                    c+=1
                    break
        return c