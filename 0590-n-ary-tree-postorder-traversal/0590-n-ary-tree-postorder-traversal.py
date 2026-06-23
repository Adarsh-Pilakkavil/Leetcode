"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        stack=[]
        if not root:
            return []
        stack.append(root)
        while stack:
            n=stack.pop()
            res.append(n.val)
            stack.extend(n.children)
        return res[::-1]