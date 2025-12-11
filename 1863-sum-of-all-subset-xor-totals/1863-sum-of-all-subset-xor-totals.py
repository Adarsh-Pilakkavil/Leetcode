class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def bt(l,index):
            if index==len(nums):
                return
            l.append(nums[index])
            xor(l)
            bt(l,index+1)
            l.pop()
            bt(l,index+1)
        def xor(l):
            nonlocal summ
            if len(l)==0:
                return
            if len(l)==1:
                summ+=l[0]
                return
            k=l[0]
            for i in range(1,len(l),1):
                k=k^l[i]
            summ+=k
            return
        summ=0
        bt([],0)
        return summ