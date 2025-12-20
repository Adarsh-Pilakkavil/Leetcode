class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        l=[str(x) for x in range(1,n+1)]
        s=''
        def bt(l,res):
            nonlocal k
            nonlocal s
            if k==0:
                return
            if l==[]:
                k-=1
                if k==0:
                    s=res
            for i in range(len(l)):
                bt(l[:i]+l[i+1:],res+l[i])
        bt(l,"")
        return s