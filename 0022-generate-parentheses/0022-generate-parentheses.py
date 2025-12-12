class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l=[]
        def bt(res,i,j):
            if i==0:
                l.append(res+")"*j)
                return
            bt(res+"(",i-1,j)
            if i<j:
                bt(res+")",i,j-1)
            return
        bt("",n,n)
        return l
