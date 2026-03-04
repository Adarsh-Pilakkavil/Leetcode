import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            h1=heapq.heappop(stones)
            h2=heapq.heappop(stones)
            if h1-h2==0:
                continue
            heapq.heappush(stones,h1-h2)
        if len(stones):
            return -stones[0]
        return 0
