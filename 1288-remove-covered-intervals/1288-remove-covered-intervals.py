class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        for i in range(len(intervals)):
            for j in range(0,len(intervals)-i-1):
                if intervals[j+1][0]<intervals[j][0] or (intervals[j+1][0]==intervals[j][0] and intervals[j][1]<intervals[j+1][1]) :
                    intervals[j],intervals[j+1]=intervals[j+1],intervals[j]
        print(intervals)
        m=intervals[0][1]
        c=0
        for i in range(1,len(intervals)):
            if intervals[i][1]<=m:
                c+=1
            else:
                m=intervals[i][1]
        return len(intervals)-c