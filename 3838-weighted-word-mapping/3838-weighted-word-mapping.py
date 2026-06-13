class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        t=""
        for i in words:
            s=0
            for j in i:
                s+=weights[ord(j)-97]
            s=s%26
            t+=str(chr(122-s))
        return t