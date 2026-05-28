# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        c=""
        def bt(s,root):
            nonlocal c
            s+=chr(97+root.val)
            if not root.left and not root.right:
                if c=="":
                    c=s[::-1]
                elif s[::-1]<c:
                    c=s[::-1]
                return
            if root.left:
                bt(s,root.left)
            if root.right:
                bt(s,root.right)
        bt("",root)
        return c