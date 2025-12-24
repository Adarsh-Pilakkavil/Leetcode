class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i in s:
            if stack and i=="*":
                stack.pop()
            else:
                if i=="*":
                    continue
                stack.append(i)
        return "".join(stack)