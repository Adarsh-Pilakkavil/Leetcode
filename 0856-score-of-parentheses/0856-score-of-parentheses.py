class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        c=0
        stack=[]
        prev=None
        for i in s:
            if i=="(":
                stack.append("(")
            else:
                stack.pop()
                if prev=="(":
                    c+=2**(len(stack))
            prev=i
        return c