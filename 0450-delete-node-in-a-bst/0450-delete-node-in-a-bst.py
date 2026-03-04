# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val>key:
            root.left=self.deleteNode(root.left,key)
        elif root.val<key:
            root.right=self.deleteNode(root.right,key)
        else:
            if root.left==None and root.right==None:
                return None
            elif root.left==None:
                return root.right
            elif root.right==None:
                return root.left
            else:
                t=root.right
                while t.left!=None:
                    t=t.left
                root.val=t.val
                root.right=self.deleteNode(root.right,root.val)
        return root
