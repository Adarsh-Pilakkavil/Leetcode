class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        l=[]
        for i in range(len(height)):
            if i==0:
                continue
            if height[i-1]>threshold:
                l.append(i)
        return l