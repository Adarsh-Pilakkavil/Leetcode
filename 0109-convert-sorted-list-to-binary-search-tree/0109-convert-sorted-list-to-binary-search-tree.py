# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self,l):
        if not l:
            return
        if l.next==None:
            return TreeNode(l.val)
        slow=l
        prev=l
        fast=l
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        root=TreeNode(slow.val)
        root.right=self.build(slow.next)
        prev.next=None
        root.left=self.build(l)
        return root
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return self.build(head)