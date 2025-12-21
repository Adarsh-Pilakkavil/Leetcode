class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title+=" "
        k=''
        c=0
        word=""
        for i in title:
            if i==" ":
                if len(word)>2:
                    k+=word[0].upper()+word[1:].lower()
                else:
                    k+=word.lower()
                word=""
                k+=" "
            else:
                word+=i
        return k[:-1]