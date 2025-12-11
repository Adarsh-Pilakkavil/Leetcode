class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        l=[first]
        for i in encoded:
            l.append(l[-1]^i)
        return l