class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        l=[x for x in range(1,k+1,1)]
        c=0
        k=[]
        while nums!=[]:
            c+=1
            t=nums.pop()
            k.append(t)
            if t in l:
                l.remove(t)
            if l==[]:
                return c
        return c