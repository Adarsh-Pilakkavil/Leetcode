class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for i in magazine:
            if i in ransomNote:
                k=ransomNote.find(i)
                ransomNote=ransomNote[:k]+ransomNote[k+1:]
        if ransomNote=="":
            return True
        else:
            return False
        