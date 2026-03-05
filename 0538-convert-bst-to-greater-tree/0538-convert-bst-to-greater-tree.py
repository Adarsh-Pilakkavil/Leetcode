# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s=[]
        k=0
        c=root
        t=c
        while root or s:
            while root:
                s.append(root)
                root=root.left
            root=s.pop()
            k+=root.val
            root=root.right
        while c or s:
            while c:
                s.append(c)
                c=c.left
            c=s.pop()
            c.val,k=k,k-c.val
            c=c.right
        return t