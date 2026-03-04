# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        s=0
        def f(root,c):
            nonlocal s
            if root.left==None and root.right==None:
                c+=str(root.val)
                s+=int(c)
                return 0
            elif root.left==None:
                c+=str(root.val)      
                return f(root.right,c)          
            elif root.right==None:
                c+=str(root.val)      
                return f(root.left,c)
            else:
                c+=str(root.val)      
                return f(root.left,c)+f(root.right,c)
        f(root,"")
        return s