class Solution:
    def trap(self, height: List[int]) -> int:
        s=[]
        ans=0
        for i in range(len(height)):
            while s and height[i]>=height[s[-1]]:
                k=s.pop()
                if not s:
                    break
                l=s[-1]
                h=min(height[i],height[s[-1]])-height[k]
                w=i-s[-1]-1
                ans+=h*w
            s.append(i)
        return ans