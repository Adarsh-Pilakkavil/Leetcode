class Solution:
    def diagonalSort(self, grid: List[List[int]]) -> List[List[int]]:
        ans=[[0]*len(grid[0]) for i in range(len(grid))]
        for i in range(len(grid)):
            j=0
            l=[]
            while i+j<len(grid) and j<len(grid[0]):
                l.append(grid[i+j][j])
                j+=1
            l.sort()
            j=0
            while i+j<len(grid) and j<len(grid[0]):
                ans[i+j][j]=l[j]
                j+=1
        for i in range(len(grid[0])):
            j=0
            l=[]
            while i+j<len(grid[0]) and j<len(grid):
                l.append(grid[j][i+j])
                j+=1
            l.sort()
            j=0
            while i+j<len(grid[0]) and j<len(grid):
                ans[j][i+j]=l[j]
                j+=1 
        return ans