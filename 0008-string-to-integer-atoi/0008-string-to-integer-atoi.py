class Solution:
    def myAtoi(self, s: str) -> int:
        lz=0
        white=True
        sign="+"
        done=True
        i=0
        num=0
        while i<len(s):
            if s[i]==" ":
                if not white:
                    break
                i+=1
                continue
            else:
                white=False
                if (s[i]=="-" or s[i]=="+"):
                    if not done:
                        break
                    done=False
                    sign=s[i]
                    i+=1
                    continue
                else:
                    done=False
                    if lz==0 and s[i]=="0":
                        i+=1
                        continue
                    elif s[i] in "0123456789":
                        lz=1
                        num=num*10+int(s[i])
                        i+=1
                    else:
                        break
        if sign=="-":
            if num>2**31:
                return -2**31
            return -num
        if num>2**31-1:
            return 2**31-1
        return num
                    

                
                