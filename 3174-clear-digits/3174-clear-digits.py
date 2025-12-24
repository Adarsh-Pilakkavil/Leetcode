class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in s:
            if 48<=ord(i) and 57>=ord(i):
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)