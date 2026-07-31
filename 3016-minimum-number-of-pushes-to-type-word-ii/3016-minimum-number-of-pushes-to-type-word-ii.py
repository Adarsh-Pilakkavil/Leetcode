class Solution:
    def minimumPushes(self, word: str) -> int:
        d={}
        for i in word:
            d[i]=d.get(i,0)+1
        n=len(d)
        l=list(d.values())
        l.sort(reverse=True)
        i=0
        c=0
        t=0
        print(l)
        while i!=len(l):
            if i%8==0:
                t+=1
            c+=t*l[i]
            i+=1
        return c