class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        pre=[0]*len(stones)
        pre[0]=stones[0]
        for i in range(len(stones)):
            pre[i]=pre[i-1]+stones[i]
        a=pre[-1]
        for i in range(len(stones)-2,0,-1):
            a=max(a,pre[i]-a)
        return a
