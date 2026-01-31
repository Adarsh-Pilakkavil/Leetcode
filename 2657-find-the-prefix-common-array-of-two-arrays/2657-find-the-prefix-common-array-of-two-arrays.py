class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        la=[]
        lb=[]
        c=0
        res=[]
        for i in range(len(A)):
            if A[i]in lb:
                c+=1
            if B[i] in la:
                c+=1
            if A[i]==B[i]:
                c+=1
            la.append(A[i])
            lb.append(B[i])
            res.append(c)
        return res