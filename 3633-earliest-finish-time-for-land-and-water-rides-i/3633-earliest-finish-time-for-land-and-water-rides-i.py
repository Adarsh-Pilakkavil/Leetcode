class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        minl=5000
        minw=minl
        res=minl
        n=len(landStartTime)
        m=len(waterStartTime)
        for i in range(n):
            minl=min(minl,landStartTime[i]+landDuration[i])
        for i in range(m):
            minw=min(minw,waterStartTime[i]+waterDuration[i])
            res=min(res,max(minl,waterStartTime[i])+waterDuration[i])
        for i in range(n):
            res=min(res,max(minw,landStartTime[i])+landDuration[i])
        return res