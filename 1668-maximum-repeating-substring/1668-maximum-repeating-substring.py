class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        c=0
        if word==sequence:
            return 1
        for i in range(1,len(sequence)+1):
            if word*i in sequence:
                c=i
            else:
                break
        return c