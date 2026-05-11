# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q=deque()
        q.append(root)
        c=0
        s=[]
        while q:
            for i in range(len(q)):
                n=q.popleft()
                if c%2==1 and s:
                    n.val=s.pop()
                if n.left:
                    if c%2==0:
                        s.append(n.left.val)
                    q.append(n.left)
                if n.right:
                    if c%2==0:
                        s.append(n.right.val)
                    q.append(n.right)
            c+=1
        return root