class Solution(object):
    def maximumScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        su=[0]*len(nums)
        su[-1]=nums[-1]
        for i in range (len(nums)-2,-1,-1):
            su[i]=min(nums[i],su[i+1])
        pre=0
        score=-10**20
        for i in range(len(nums)-1):
            pre+=nums[i]
            score=max(score,pre-su[i+1])
        return score 