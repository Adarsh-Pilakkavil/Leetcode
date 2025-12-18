class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        prev=nums[0]
        curr=nums[1]
        for i in range(2,len(nums),1):
            if curr==prev:
                return curr
            else:
                prev=curr
                curr=nums[i]
        if curr==prev:
            return curr