class Solution:
    def restoreString(self, c: str, indices: List[int]) -> str:
        s=[0]*len(indices)
        for i in range(len(indices)):
            s[indices[i]]=c[i]
        return "".join(s)