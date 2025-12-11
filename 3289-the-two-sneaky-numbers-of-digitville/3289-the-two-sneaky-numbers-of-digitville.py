class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        k=[]
        s=[]
        for i in nums:
            if i in k:
                s.append(i)
            else:
                k.append(i)
        return s
        