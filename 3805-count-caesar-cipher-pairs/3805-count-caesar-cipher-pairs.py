class Solution:
    def countPairs(self, words: List[str]) -> int:
        d={}
        l=[]
        for i in words:
            s=ord(i[0])-97
            n=""
            for ch in i:
                v=ord(ch)-s
                if v<97:
                    v+=26
                n+=chr(v)
            l.append(n)
        c=0
        for i in l:
            d[i]=d.get(i,0)+1
        for i in d:
            c+=(d[i]*d[i]-d[i])//2
        return c