# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        s=[]
        l=[]
        c=float("inf")
        while s or root:
            while root:
                s.append(root)
                root=root.left
            root=s.pop()
            l.append(root.val)
            root=root.right
        for i in range(len(l)-1):
            if l[i+1]-l[i]<c:
                c=l[i+1]-l[i]
        return c
