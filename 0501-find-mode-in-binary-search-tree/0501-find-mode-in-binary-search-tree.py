# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        c=0
        s=[]
        d={}
        while s or root:
            while root:
                s.append(root)
                root=root.left
            root=s.pop()
            d[root.val]=1+d.get(root.val,0)
            if d[root.val]>c:
                c=d[root.val]
                x=[root.val]
            elif d[root.val]==c:
                x.append(root.val)
            root=root.right
        return x