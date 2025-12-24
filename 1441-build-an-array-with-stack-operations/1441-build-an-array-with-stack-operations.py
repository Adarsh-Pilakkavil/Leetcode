class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s=[]
        k=[]
        for i in range(1,n+1,1):
            if k==target:
                break
            if i in target:
                k.append(i)
                s.append("Push")
            else:
                s.append("Push")
                s.append("Pop")
        return s