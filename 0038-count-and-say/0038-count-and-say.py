class Solution(object):
    def countAndSay(self, n):
        def foo(n):
            if n==1:
                return "1"
            k=foo(n-1)
            s=""
            candidate=k[0]
            count=0
            for i in range(0,len(k),1):
                if candidate==k[i]:
                    count+=1
                else:
                    s+=str(count)+candidate
                    count=1
                    candidate=k[i]
            s+=str(count)+candidate
            return s
        return foo(n)
            
                

        