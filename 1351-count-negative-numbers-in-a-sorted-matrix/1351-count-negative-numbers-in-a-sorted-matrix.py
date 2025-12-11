class Solution:
    def bs(self,ar):
        st=0
        en=len(ar)-1
        while st<=en:
            mid=(st+en)//2
            if ar[mid]<0:
                en=mid-1
            else:
                st=mid+1
        return len(ar)-st
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([self.bs(arr) for arr in grid])