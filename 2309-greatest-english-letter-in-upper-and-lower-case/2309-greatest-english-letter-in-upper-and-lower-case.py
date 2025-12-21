class Solution:
    def greatestLetter(self, s: str) -> str:
        for i in range(122,96,-1):
            if chr(i) in s and chr(i-32) in s:
                return chr(i-32)
        return ""
        