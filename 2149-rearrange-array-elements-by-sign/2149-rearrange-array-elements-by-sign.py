class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        l=[]
        for i in range(len(nums)):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        for i in range(len(pos)):
            l.append(pos[i])
            l.append(neg[i])
        return l
