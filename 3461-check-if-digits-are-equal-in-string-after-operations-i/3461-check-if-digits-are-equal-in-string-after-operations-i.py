class Solution:
    def hasSameDigits(self, s: str) -> bool:
        t=s
        while len(t)!=2:
            k=''
            for i in range(len(t)-1):
                k+=str((int(t[i])+int(t[i+1]))%10)
            print(k)
            t=k
        if t[0]==t[1]:
            return True
        return False