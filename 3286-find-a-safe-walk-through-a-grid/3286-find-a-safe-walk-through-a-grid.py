class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        memo=[[float("inf")]*len(grid[0]) for i in range(len(grid))]

        def dfs(i, j, l, health, memo):
            if health <= 0:
                return False
            if i < 0 or i >= len(l) or j < 0 or j >= len(l[0]):
                return False
            health -= l[i][j]
            if memo[i][j]!=float("inf"):
                if memo[i][j]<health:
                    memo[i][j]=health
                else:
                    return False
            else:
                memo[i][j]=health
            if i == len(l) - 1 and j == len(l[0]) - 1:
                if health > 0:
                    return True
                return False
            return (
                dfs(i + 1, j, l, health,memo)
                or dfs(i, j + 1, l, health, memo)
                or dfs(i - 1, j, l, health, memo)
                or dfs(i, j - 1, l, health, memo)
            )

        return dfs(0, 0, grid, health, memo)