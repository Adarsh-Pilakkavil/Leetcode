# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self,root,l,left,right):
        if left>right:
            return 
        mid=(left+right)//2
        root=TreeNode(l[mid])
        root.left=self.build(root,l,left,mid-1)
        root.right=self.build(root,l,mid+1,right)
        return root
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s=[]
        l=[]
        while root or s:
            while root:
                s.append(root)
                root=root.left
            root=s.pop()
            l.append(root.val)
            root=root.right
        c=self.build(None,l,0,len(l)-1)
        return c