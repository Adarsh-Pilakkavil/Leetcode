class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        am=minutes*6
        ah=(hour%12)*30+minutes*0.5
        d=abs(am-ah)
        if d>180:
            return 360-d
        return d