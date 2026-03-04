# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def ch(root,mi,ma):
            if not root:
                return True
            if not root.val>mi or not root.val<ma:
                return False
            if root.right==None and root.left==None:
                return True
            else:
                return ch(root.right,root.val,ma) and ch(root.left,mi,root.val)
        return ch(root,-(2**31)-1,2**31)