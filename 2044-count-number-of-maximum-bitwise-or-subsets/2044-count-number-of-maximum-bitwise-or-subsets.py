class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        k=0
        c=0
        for i in nums:
            k=k|i
        def bt(i,l):
            nonlocal c
            if i==len(nums):
                t=0
                for i in l:
                    t=t|i
                if t==k:
                    c+=1
                return
            l.append(nums[i])
            bt(i+1,l)
            l.pop()
            bt(i+1,l)
            return
        bt(0,[])
        return c
