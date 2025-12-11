class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        s=bin(n)[2:]
        s=s[::-1]
        even,odd=0,0
        for i in range(len(s)):
            if s[i]=='1':
                if i%2==0:
                    even+=1
                else:
                    odd+=1
        return [even,odd]