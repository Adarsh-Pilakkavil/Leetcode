class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        k="aeiou"
        c=0
        for i in range(left,right+1):
            if words[i][0] in k and words[i][-1] in k:
                c+=1
        return c