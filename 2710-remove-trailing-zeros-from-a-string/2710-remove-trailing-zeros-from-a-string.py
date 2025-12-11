class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        i=-1
        while True:
            if num[i]=="0":
                i-=1
                continue
            else:
                i+=1
                break
        if i==0:
            return num
        return num[:i:1]