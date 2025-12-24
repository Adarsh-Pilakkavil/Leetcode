# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=head
        fast=head.next.next
        m=0
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        curr,prev=slow,None
        while curr!=None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        while prev!=None and head!=None:
            m=max(m,head.val+prev.val)
            head=head.next
            prev=prev.next
        return m