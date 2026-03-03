# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        res=True
        q=deque()
        q.append(root)
        while q:
            level=[]
            l=len(q)
            for i in range(l):
                n=q.popleft()
                if n.left:
                    q.append(n.left)
                    level.append(n.left.val)
                else:
                    level.append(-500)
                if n.right:
                    q.append(n.right)
                    level.append(n.right.val)
                else:
                    level.append(-500)
            if level==level[::-1] and len(level)%2==0:
                continue
            else:
                res=False
                break
        return res