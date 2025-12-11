class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        curr=nums[0]
        count=1
        maxx=1
        for i in nums:
            if i>curr:
                count+=1
                if count>maxx:
                    maxx=count
            else:
                count=1
            curr=i
        return maxx
                