class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i.isdigit() or i[1:].isdigit():
                stack.append(int(i))
            elif i=="+":
                k=stack.pop()+stack.pop()
                stack.append(k)
            elif i=="-":
                n1=stack.pop()
                n2=stack.pop()
                stack.append(n2-n1)
            elif i=="*":
                k=stack.pop()*stack.pop()
                stack.append(k)
            elif i=="/":
                n1=stack.pop()
                n2=stack.pop()
                if n2//n1>=0:
                    stack.append(n2//n1)
                elif n2//n1==n2/n1:
                    stack.append(n2//n1)
                else:
                    stack.append(n2//n1+1)
        return stack.pop()
