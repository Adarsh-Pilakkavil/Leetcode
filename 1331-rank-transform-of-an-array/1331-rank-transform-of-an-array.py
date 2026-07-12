class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d={}
        l=sorted(arr)
        c=1
        for i in range(len(l)):
            if l[i] in d:
                continue
            d[l[i]]=c
            c+=1
        ans=[]
        for i in arr:
            ans.append(d[i])
        return ans