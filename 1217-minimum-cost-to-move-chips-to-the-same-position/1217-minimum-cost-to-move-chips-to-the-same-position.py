class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        o=0
        e=0
        for i in position:
            if i%2==0:
                e+=1
            else:
                o+=1
        return min(e,o)