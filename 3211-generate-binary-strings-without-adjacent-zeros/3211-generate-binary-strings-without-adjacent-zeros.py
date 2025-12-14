class Solution:
    def validStrings(self, n: int) -> List[str]:
        l=[]
        def bt(i,s):
            if i==0:
                l.append(s)
                return
            if s!="" and s[-1]=="0":
                s+="1"
                bt(i-1,s)
            else:
                bt(i-1,s+"0")
                bt(i-1,s+"1")
            return
        bt(n,"")
        return l