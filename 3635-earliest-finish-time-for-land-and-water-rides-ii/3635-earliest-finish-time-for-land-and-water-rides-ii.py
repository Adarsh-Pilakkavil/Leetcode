class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        minl=10**6
        minw=minl
        res=minl
        for i in range(len(landStartTime)):
            minl=min(minl,landStartTime[i]+landDuration[i])
        for i in range(len(waterStartTime)):
            minw=min(minw,waterStartTime[i]+waterDuration[i])
            res=min(res,max(minl,waterStartTime[i])+waterDuration[i])
        for i in range(len(landStartTime)):
            res=min(res,max(minw,landStartTime[i])+landDuration[i])
        return res