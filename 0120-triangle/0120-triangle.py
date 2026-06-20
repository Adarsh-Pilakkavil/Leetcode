class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp={}
        def rec(row,col):
            if row==len(triangle):
                return 0
            if (row,col) in dp:
                return dp[(row,col)]
            l=rec(row+1,col)
            r=rec(row+1,col+1)
            dp[(row,col)]=triangle[row][col]+min(l,r)
            return dp[(row,col)]
        return rec(0,0)