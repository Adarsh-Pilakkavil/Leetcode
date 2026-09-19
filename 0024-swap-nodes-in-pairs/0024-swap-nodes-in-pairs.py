# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rec(prev,head):
            if not head or not head.next:
                return 
            x=head.next
            nxt=x.next
            head.next=nxt
            if not prev:
                prev=head
            else:
                prev.next=x
            x.next=head
            prev=head
            rec(prev,nxt)
            return x
        if not head or not head.next:
            return head
        return rec(None,head)