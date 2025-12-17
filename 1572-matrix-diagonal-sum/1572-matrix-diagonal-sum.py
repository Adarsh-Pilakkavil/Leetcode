class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        c=0
        for i in range(n):
            c+=mat[i][i]+mat[i][n-i-1]
        if n%2==1:
            return c-mat[n//2][n//2]
        else:
            return c
