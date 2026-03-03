# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def l(r):
            if r is None:
                return 0
            return 1+max(l(r.right),l(r.left))
        def rec(r):
            if r is None:
                return True
            if l(r.right)-l(r.left) in [-1,0,1]:
                return rec(r.right) and rec(r.left)
            return False
        return rec(root)