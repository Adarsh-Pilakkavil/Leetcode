class Solution(object):
    def plusOne(self, digits):
        j=0
        k=1
        for i in digits:
            j+=i*(10**(len(digits)-k))
            k+=1
        j+=1
        k=str(j)
        s=[]
        for i in k:
            s.append(int(i))
        return s
        