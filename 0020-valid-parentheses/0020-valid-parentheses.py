class Solution(object):
    def isValid(self, s):
        l=[]
        if len(s)%2==1:
            return False
        for i in range(0,len(s),1):
            if s[i] =='(' or s[i] =='[' or s[i] =='{':
                l.append(s[i])
            else:
                if l==[]:
                    return False
                if l[len(l)-1]=='(' and s[i]==")":
                    l.pop()
                elif l[len(l)-1]=='[' and s[i]=="]":
                    l.pop() 
                elif l[len(l)-1]=='{' and s[i]=="}":
                    l.pop()
                else:
                    return False
                    exit()
        if l==[]:
            return True
        else:
            return False