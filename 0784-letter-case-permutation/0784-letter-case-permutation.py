class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        l=[]
        def bt(res,i):
            if i==len(s):
                if res not in l:
                    l.append(res)
                return
            bt(res+(s[i].upper()),i+1)
            bt(res+(s[i].lower()),i+1)
        bt("",0)
        return l