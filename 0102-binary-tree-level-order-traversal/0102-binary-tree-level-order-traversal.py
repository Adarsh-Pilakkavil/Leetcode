# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        s=[root]
        while s:
            t=[]
            l=[]
            for j in s:
                l.append(j.val)
                if j.left:   
                    t.append(j.left)
                if j.right:
                    t.append(j.right)
            s=t
            res.append(l)
        return res
                                 