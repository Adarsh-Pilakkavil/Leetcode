class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=[]
        l=["A","E","I","O","U","a","e","i","o","u"]
        for i in s:
            if i in l:
                vowels.append(i)
        vowels.sort()
        c=0
        k=""
        for i in range(len(s)):
            if s[i] in l:
                k+=vowels[c]
                c+=1
            else:
                k+=s[i]
        return k