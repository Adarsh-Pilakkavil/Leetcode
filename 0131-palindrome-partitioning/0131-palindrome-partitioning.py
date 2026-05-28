class Solution:
    def partition(self, s: str) -> List[List[str]]:
        l=[]
        def bt(k,s):
            nonlocal l
            if len(s)==0:
                for i in k:
                    if i!=i[::-1]:
                        return
                l.append(k[:])
                return
            for i in range(1,len(s)+1):
                k.append(s[:i])
                bt(k,s[i:])
                k.pop()
        bt([],s)
        return l