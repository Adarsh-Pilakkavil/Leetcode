# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr=root
        f=TreeNode(val)
        if root ==None:
            return f
        while curr:
            if curr.val>val:
                if curr.left==None:
                    curr.left=f
                    break
                curr=curr.left
            else:
                if curr.right==None:
                    curr.right=f
                    break
                curr=curr.right
        return root