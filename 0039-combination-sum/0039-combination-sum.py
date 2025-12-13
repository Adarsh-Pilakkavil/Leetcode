class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l=[]
        def bt(start,res,t):
            if t<=0 or start==len(candidates):
                if t==0:
                    l.append(res[:])
                return
            for i in range(start,len(candidates)):
                res.append(candidates[i])
                bt(i,res,t-candidates[i])
                res.pop()
            return 
        bt(0,[],target)
        return l