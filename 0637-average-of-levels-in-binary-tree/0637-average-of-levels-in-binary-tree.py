# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=deque()
        if not root:
            return []
        res=[]
        q.append(root)
        level=[root.val]
        while level:
            res.append(sum(level)/len(level))
            l=len(q)
            level=[]
            for i in range(l):
                n=q.popleft()
                if n.left:
                    q.append(n.left)
                    level.append(n.left.val)
                if n.right:
                    q.append(n.right)
                    level.append(n.right.val)
        return res
            