class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for i in range(low,high+1,1):
            if len(str(i))%2==1:
                continue
            k=list(str(i)[:len(str(i))//2])
            k=[int(x) for x in k]
            sum1=sum(k)
            k=list(str(i)[len(str(i))//2:])
            k=[int(x) for x in k]
            sum2=sum(k)
            if sum1==sum2:
                count+=1
        return count