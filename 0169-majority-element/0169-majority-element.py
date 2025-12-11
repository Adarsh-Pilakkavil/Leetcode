class Solution(object):
    def majorityElement(self, nums):
        count=0
        candidate=nums[0]
        for i in nums:
            if i==candidate:
                count+=1
            else:
                if count>0:
                    count-=1
                else:
                    candidate=i
                    count+=1
        return candidate
        
        