class Solution(object):
    def fizzBuzz(self, n):
        l=[]
        for i in range(1,n+1,1):
            if i%3==0 and i%5==0:
                l.append("FizzBuzz")
                continue
            if i%3==0:
                l.append("Fizz")
                continue
            if i%5==0:
                l.append("Buzz")
                continue
            l.append(str(i))
        return l

        