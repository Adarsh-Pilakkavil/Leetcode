class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        i=0
        res=0
        while i<len(heights):
            if stack==[] or heights[i]>heights[stack[-1]]:
                stack.append(i)
            else:
                curr=stack.pop()
                t=i if stack==[] else i-stack[-1]-1
                res=max(res,t*heights[curr])
                i-=1
            i+=1
        while stack!=[]:
            curr=stack.pop()
            t=len(heights) if stack==[] else len(heights)-stack[-1]-1
            res=max(res,t*heights[curr])
        return res