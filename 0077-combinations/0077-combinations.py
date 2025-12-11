class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        nums=[x for x in range(1,n+1,1)]
        def bt(i,l):
            if len(l)==k:
                result.append(l[:])
                return
            for t in range(i,n):
                l.append(nums[t])
                bt(t+1,l)
                l.pop()
        bt(0,[])
        return result            