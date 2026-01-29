class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        k=''
        c=0
        for i in s:
            if i=="(":
                c+=1
                k+="("
            elif i==")" and c>0:
                c-=1
                k+=")"
            elif i==")" and c<=0:
                continue
            else:
                k+=i
        s=""
        c=0
        for i in range(len(k)-1,-1,-1):
            if k[i]==")":
                c+=1
                s=")"+s
            elif k[i]=="(" and c>0:
                c-=1
                s="("+s
            elif k[i]=="(" and c<=0:
                continue
            else:
                s=k[i]+s
        return s
        
        
            