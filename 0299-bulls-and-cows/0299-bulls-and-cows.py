class Solution(object):
    def getHint(self, secret, guess):
        lt=[]
        lf=[]
        b,c=0,0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                b+=1
                lt.append(i)
            else: 
                lf.append(secret[i])
        for i in range(len(secret)):
            if i in lt:
                continue
            if guess[i] in lf:
                lf.remove(guess[i])
                c+=1
        return str(b)+"A"+str(c)+"B"
        