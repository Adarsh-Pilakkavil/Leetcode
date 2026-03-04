# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        s=[]
        while root or s:
            while root:
                s.append(root)
                root=root.left
            root=s.pop()
            res.append(root.val)
            k-=1
            if k==0:
                return res.pop()
            root=root.right
        return res