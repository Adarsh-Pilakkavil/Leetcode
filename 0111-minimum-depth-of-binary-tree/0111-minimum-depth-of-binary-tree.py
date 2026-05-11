# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q=deque()
        if not root:
            return 0
        q.append(root)
        c=1
        while q:
            for i in range(len(q)):
                n=q.popleft()
                if not n.left and not n.right:
                    return c
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            c+=1
        return c