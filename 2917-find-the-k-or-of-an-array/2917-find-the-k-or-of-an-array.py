class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        s=''
        for i in range(0,32,1):
            y=[x%2 for x in nums]
            if y.count(1)>=k:
                s+='1'
            else:
                s+='0'
            nums=[x>>1 for x in nums]
        s=s[::-1]
        return int(s,2)


        