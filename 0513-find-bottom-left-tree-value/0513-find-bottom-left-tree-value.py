# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append(root)
        temp=deque()
        while q:
            t=len(q)
            temp=deque(q)
            for i in range(t):
                n=q.popleft()
                if n.left!=None:
                    q.append(n.left)
                if n.right!=None:
                    q.append(n.right)
        return temp[0].val