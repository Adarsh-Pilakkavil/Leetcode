class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sum1=0
        sum2=0
        for i in nums:
            if i>9:
                sum1+=i
            else:
                sum2+=i
        if sum1==sum2:
            return False
        return True