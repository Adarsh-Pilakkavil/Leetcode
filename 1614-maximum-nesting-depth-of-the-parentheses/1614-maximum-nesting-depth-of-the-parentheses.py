class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        m=0
        for i in s:
            if i=="(":
                stack.append("(")
            elif i==")":
                m=max(len(stack),m)
                stack.pop()
            else:
                continue
        return m