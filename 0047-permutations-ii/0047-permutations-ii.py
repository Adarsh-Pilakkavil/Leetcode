class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        index=[-11]*len(nums)
        res=[]
        def rec(i,nums,index):
            nonlocal res
            if i==len(nums):
                if index[:] in res:
                    return
                res.append(index[:])
                return
            for j in range(len(nums)):
                if index[j]==-11:
                    index[j]=nums[i]
                    rec(i+1,nums,index[:])
                    index[j]=-11
        rec(0,nums,index)
        return res