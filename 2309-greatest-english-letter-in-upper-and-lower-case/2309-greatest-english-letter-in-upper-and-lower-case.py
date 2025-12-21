class Solution:
    def greatestLetter(self, s: str) -> str:
        m=""
        for i in s:
            if i.upper() in s and i.lower() in s:
                if m=="":
                    m=i
                else:
                    if ord(i)>ord(m):
                        m=i
        return m.upper()
        