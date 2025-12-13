class Solution:
    def punishmentNumber(self, n: int) -> int:
        def bt(s,idx,target):
            if idx==len(s):
                return target==0
            num=0
            for i in range(idx,len(s)):
                num=num*10+int(s[i])
                if num>target:
                    break
                if bt(s,i+1,target-num):
                    return True
            return False
        ans=0
        for i in range(1,n+1,1):
            if bt(str(i*i),0,i):
                ans+=(i*i)
        return ans