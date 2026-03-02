# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q=deque()
        if not root:
            return []
        level=[root.val]
        q.append(root)
        while level:
            res.append(level)
            l=len(q)
            level=[]
            for i in range(l):
                n=q.popleft()
                if n.left:
                    level.append(n.left.val)
                    q.append(n.left)
                if n.right:
                    level.append(n.right.val)
                    q.append(n.right)
        return res[::-1]