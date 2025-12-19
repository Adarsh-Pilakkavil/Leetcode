class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        l=[[k,k] for k in range(n)]
        l.extend([[k,n-k-1] for k in range(n)])
        print(l)
        for i in range(n):
            for j in range(n):
                if [i,j] in l:
                    if grid[i][j]==0:
                        return False
                else:
                    if grid[i][j]!=0:
                        return False
        return True