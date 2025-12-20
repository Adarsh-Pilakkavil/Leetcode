# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum=ListNode(0,head)
        prev=dum
        while head:
            if head.next and head.val==head.next.val:
                dup=head.val
                while head and head.val==dup:
                    head=head.next
                prev.next=head
            else:
                prev=head
                head=head.next
        return dum.next
            