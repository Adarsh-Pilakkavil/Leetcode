class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n=0
        for i in range(len(num)):
            n=n*10+num[i]
        n=n+k
        l=[]
        while n!=0:
            d=n%10
            l.append(d)
            n=n//10
        return l[::-1]