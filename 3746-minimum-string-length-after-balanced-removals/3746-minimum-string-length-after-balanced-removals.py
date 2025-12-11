class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        a=s.count("a")
        b=s.count("b")
        if a>b:
            return len(s)-(2*b)
        return len(s)-(2*a)