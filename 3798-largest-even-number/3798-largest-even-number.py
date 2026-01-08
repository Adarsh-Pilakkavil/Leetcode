class Solution:
    def largestEven(self, s: str) -> str:
        while s:
            if s[-1]=="2":
                return s
            s=s[:len(s)-1]
        return s