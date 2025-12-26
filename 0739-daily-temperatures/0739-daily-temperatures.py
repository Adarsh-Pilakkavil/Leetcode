class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        s=[]
        i=0
        while i!=len(temperatures):
            if s and temperatures[i]>temperatures[s[-1]]:
                k=i-s[-1]
                res[s.pop()]=k
                continue
            s.append(i)
            i+=1
        return res