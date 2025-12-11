class Solution(object):
    def addBinary(self, a, b):
        n1,n2=0,0
        for i in range(0,len(a),1):
            n1+=int(a[i])*(2**(len(a)-1-i))
        for i in range(0,len(b),1):
            n2+=int(b[i])*(2**(len(b)-1-i))
        return str(bin(n1+n2))[2::]
        