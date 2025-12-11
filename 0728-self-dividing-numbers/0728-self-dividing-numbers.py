class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l=[]
        def f(x):
            s=str(x)
            if "0" in s:
                return False
            for k in s:
                if x%int(k)!=0:
                    return False
            return True
        for i in range(left,right+1,1):
            if f(i):
                l.append(i)
        return l