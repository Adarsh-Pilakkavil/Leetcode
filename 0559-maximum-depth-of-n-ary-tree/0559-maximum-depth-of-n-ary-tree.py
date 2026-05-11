"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        q=deque()
        if not root:
            return 0
        c=0
        q.append(root)
        while q:
            for i in range(len(q)):
                n=q.popleft()
                for i in n.children:
                    q.append(i)
            c+=1
        return c