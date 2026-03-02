# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def rec(t):
            if t is None:
                return
            rec(t.left)
            res.append(t.val)
            rec(t.right)
        rec(root)
        return res