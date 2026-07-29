class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l=intervals[0][0]
        h=intervals[0][1]
        ans=[]
        for i in range(1,len(intervals)):
            if intervals[i][0]<=h:
                h=max(h,intervals[i][1])
            else:
                ans.append([l,h])
                l=intervals[i][0]
                h=intervals[i][1]
        ans.append([l,h])
        return ans