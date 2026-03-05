# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        l=[]
        if not root:
            return []
        def f(r,p,t):
            nonlocal l
            if not r:
                return
            p.append(r.val)
            if r.right==None and r.left==None:
                print(p)
                if t==r.val:
                    l.append(p[:])
            f(r.left,p,t-r.val)
            f(r.right,p,t-r.val)
            p.pop()
        f(root,[],targetSum)
        return l