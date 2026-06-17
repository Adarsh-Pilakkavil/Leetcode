class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        rows=[[] for r in range(numRows)]
        i=0
        step=-1
        for ch in s:
            rows[i].append(ch)
            if i==0:
                step=1
            elif i==numRows-1:
                step=-1
            i+=step
        for i in range(numRows):
            rows[i]="".join(rows[i])
        return "".join(rows)
            