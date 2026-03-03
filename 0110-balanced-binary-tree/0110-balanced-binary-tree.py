# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans=True
        def l(r):
            if r is None:
                return 0
            c1=l(r.left)
            c2=l(r.right)
            if abs(c1-c2)>1:
                self.ans=False
            return 1+max(c1,c2)
        l(root)
        return self.ans