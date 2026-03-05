# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def su(root):
            if not root:
                return 0
            return su(root.left)+su(root.right)+root.val
        def c(root):
            if not root:
                return 0
            return c(root.left)+c(root.right)+1
        s=[root]
        count=0
        while s:
            n=s.pop()
            if su(n)//c(n)==n.val:
                count+=1
            if n.right:
                s.append(n.right)
            if n.left:
                s.append(n.left)
        return count