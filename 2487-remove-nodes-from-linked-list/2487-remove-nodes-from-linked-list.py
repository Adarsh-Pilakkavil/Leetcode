# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            pass
        else:
            curr=head
            prev=None
            while curr!=None:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
        curr=prev.next
        pre=prev
        ma=prev.val
        while curr:
            if curr.val>=ma:
                ma=curr.val
                pre.next=curr
                pre=pre.next
            curr=curr.next
        pre.next=None
        curr=prev
        head=None
        while curr!=None:
            nxt=curr.next
            curr.next=head
            head=curr
            curr=nxt
        return head