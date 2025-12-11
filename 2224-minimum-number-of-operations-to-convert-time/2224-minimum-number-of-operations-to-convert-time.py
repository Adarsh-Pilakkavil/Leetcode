class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        sum=0
        t1=int(current[:2])*60+int(current[3:])
        t2=int(correct[:2])*60+int(correct[3:])
        t=t2-t1
        sum+=t//60
        t=t%60
        sum+=t//15
        t=t%15
        sum+=t//5
        t=t%5
        sum+=t//1
        t=t%1
        return sum
        