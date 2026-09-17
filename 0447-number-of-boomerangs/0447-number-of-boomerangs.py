class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        res=0
        for p in points:
            d={}
            for q in points:
                dis=abs(q[1]-p[1])**2+abs(q[0]-p[0])**2
                d[dis]=d.get(dis,0)+1
            for c in d.values():
                res+=c*(c-1)
        return res
