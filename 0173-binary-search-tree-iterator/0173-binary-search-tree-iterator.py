# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.k=root
        self.s=[]
        self.l=[]
        self.i=0
        while self.k or self.s:
            while self.k:
                self.s.append(self.k)
                self.k=self.k.left
            self.k=self.s.pop()
            self.l.append(self.k.val)
            self.k=self.k.right
    def next(self) -> int:
        if self.i<len(self.l):
            self.i+=1
            return self.l[self.i-1]
        return 
    def hasNext(self) -> bool:
        if self.i<len(self.l):
            return True
        return False
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()