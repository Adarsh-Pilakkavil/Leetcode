class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        i=0
        while i!=len(s):
            if stack and stack[-1]=="(" and s[i]==")":
                stack.pop()
            else:
                stack.append(s[i])
            i+=1
        return len(stack)

            