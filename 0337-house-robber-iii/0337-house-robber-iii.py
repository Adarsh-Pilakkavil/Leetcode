# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def bt(root):
            if not root:
                return (0,0)
            l=bt(root.left)
            r=bt(root.right)
            in_take=root.val+l[1]+r[1]
            out_take=max(l)+max(r)
            return (in_take,out_take)
        return max(bt(root))