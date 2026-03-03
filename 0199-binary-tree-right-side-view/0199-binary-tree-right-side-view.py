# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        if not root:
            return []
        q=deque()
        q.append(root)
        level=[]
        while q:
            l=len(q)
            level=[]
            for i in range(l):
                n=q.popleft()
                level.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            if level:
                res.append(level[-1])
        return res