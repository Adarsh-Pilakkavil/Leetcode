class Solution(object):
    def longestCommonPrefix(self, strs):
        k=""
        f=strs[0]
        for i in range(0,len(strs),1):
            if len(strs[i])<len(f):
                f=strs[i]
        t=0
        for j in f:
            for i in range(0,len(strs),1):
                if j== strs[i][t]:
                    continue
                else:
                    return k
            t+=1
            k+=j
        return k