class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l=list(title.split())
        final=[]
        for i in l:
            if len(i)<=2:
                final.append(i.lower())
            else:
                k=i[0].upper()
                k+=i[1:].lower()
                final.append(k)
        return " ".join(final)