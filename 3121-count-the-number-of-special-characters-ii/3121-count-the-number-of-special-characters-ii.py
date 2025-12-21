class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ds={}
        dl={}
        c=0
        for i in range(len(word)):
            if word[i].lower()==word[i]:
                ds[word[i]]=i
            else:
                if word[i] in dl:
                    continue
                dl[word[i]]=i
        for i in ds:
            if i.upper() in dl and dl[i.upper()]>ds[i]:
                c+=1
        return c
