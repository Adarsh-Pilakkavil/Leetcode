class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        t=len(nums[0])
        l='0'
        def bt(res,k):
            nonlocal t
            nonlocal l
            if k==0:
                if res not in nums and res!="0"*t:
                    l=res
                return
            bt(res+"0",k-1)
            bt(res+"1",k-1)
        bt("",t)
        return l