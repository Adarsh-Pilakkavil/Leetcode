class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        k=len(word)
        c=0
        for i in word:
            if i.upper()==i:
                c+=1
        if c==k or c==0:
            return True
        if c==1 and word[0].upper()==word[0]:
            return True
        return False