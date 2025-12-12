class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        t=len(nums[0])
        l='0'
        m=False
        def bt(res,k):
            nonlocal t
            nonlocal l
            nonlocal m
            if m:
                return
            if k==0:
                if res not in nums and res!="0"*t:
                    l=res
                    m=True
                return
            bt(res+"0",k-1)
            bt(res+"1",k-1)
        bt("",t)
        return l