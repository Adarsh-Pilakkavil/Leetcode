# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque()
        res=[]
        level=[root.val]
        c=1
        q.append(root)
        while level:
            if c%2==1:
                res.append(level)
            else:
                res.append(level[::-1])
            c+=1
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