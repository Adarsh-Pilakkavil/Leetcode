class Solution:
    def bestClosingTime(self, customers: str) -> int:
        yes=0
        for i in customers:
            if i=="Y":
                yes+=1
        m=10**10
        t=-1
        no=0
        for i in range(len(customers)):
            if no+yes<m:
                m=no+yes
                t=i
            if customers[i]=="N":
                no+=1
            else:
                yes-=1
        if no+yes<m:
            m=no+yes
            t=len(customers)
        return t
        