class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])

        res = 0

        for r in range(self.m):
            for c in range(self.n):
                if grid[r][c]==1:
                    res = max(res, self.dfs(r, c))
        
        return res

    
    def dfs(self, r, c):
        if r >= self.m or r < 0 or c >= self.n or c < 0 or self.grid[r][c] != 1:
            return 0
        self.grid[r][c] = 0
        return 1 + self.dfs(r+1,c) + self.dfs(r-1,c) + self.dfs(r,c+1) + self.dfs(r,c-1)