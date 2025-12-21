class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        for i in range(65,91,1):
            if chr(i) in word and chr(i+32) in word:
                c+=1
        return c