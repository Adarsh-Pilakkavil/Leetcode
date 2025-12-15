class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        l=[]
        def bt(start,count,target,res):
            if target<0:
                return
            if count==0:
                if target==0:
                    l.append(res[::])
                return
            for i in range(start,10,1):
                res.append(i)
                bt(i+1,count-1,target-i,res[::])
                res.pop()
            return
        bt(1,k,n,[])
        return l