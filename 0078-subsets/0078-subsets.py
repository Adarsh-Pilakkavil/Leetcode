class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def bt(l,index):
            if index==len(nums):
                result.append(l[:])
                return 
            l.append(nums[index])
            bt(l,index+1)
            l.pop()
            bt(l,index+1)
        bt([],0)
        return result
                