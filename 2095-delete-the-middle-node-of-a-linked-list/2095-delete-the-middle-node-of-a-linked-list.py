# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        prev=None
        if not head.next:
            return head.next
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        prev.next=slow.next
        return head