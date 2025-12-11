class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        l=[]
        for i in arr:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        for i in d.values():
            if i in l:
                return False
            l.append(i)
        return True