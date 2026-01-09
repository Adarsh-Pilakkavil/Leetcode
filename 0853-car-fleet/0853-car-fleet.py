class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        c=sorted(zip(position,speed),reverse=True)
        lasttime=0
        fleet=0
        for pos,spe in c:
            time=(target-pos)/spe
            if time>lasttime:
                fleet+=1
                lasttime=time
        return fleet