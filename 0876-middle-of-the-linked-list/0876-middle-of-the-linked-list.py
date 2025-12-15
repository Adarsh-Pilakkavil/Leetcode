# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        k=0
        current=head
        while current!=None:
            k+=1
            current=current.next
        k=k//2
        current=head
        for i in range(k):
            current=current.next
        return current