class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        push=0
        popp=0
        stack=[]
        while push!=len(pushed) or popp!=len(popped):
            if stack and stack[-1]==popped[popp]:
                stack.pop()
                popp+=1
            elif stack and push==len(pushed):
                break
            else:
                stack.append(pushed[push])
                push+=1
        if not stack:
            return True
        return False
        