class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        print(candidates)
        l=[]
        def bt(start,res,t):
            if t<=0:
                if t==0 and res not in l:
                    l.append(res[:])
                return
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                res.append(candidates[i])
                bt(i+1,res,t-candidates[i])
                res.pop()
            return
        bt(0,[],target)
        return l