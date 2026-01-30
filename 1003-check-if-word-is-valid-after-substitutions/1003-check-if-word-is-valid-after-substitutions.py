class Solution:
    def isValid(self, s: str) -> bool:
        i=0
        stack=[]
        while i!=len(s):
            stack.append(s[i])
            if "".join(stack[-3::])=="abc":
                stack.pop()
                stack.pop()
                stack.pop()
            i+=1
            print(stack,"".join(stack[:-3:-1]))
        return "".join(stack)==""