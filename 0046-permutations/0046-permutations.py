class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def bt(l,index):
            if len(l)==len(nums):
                result.append(l[:])
                return
            for num in nums:
                if num in l:
                    continue
                l.append(num)
                bt(l,index+1)
                l.pop()
        bt([],0)
        return result
