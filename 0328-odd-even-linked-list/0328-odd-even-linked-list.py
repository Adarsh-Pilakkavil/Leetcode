# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        l=2
        curr=head.next
        prev=head
        tail=head
        le=1
        while tail.next!=None:
            le+=1
            tail=tail.next
        while curr!=None:
            if l<=le:
                prev.next=curr.next
                tail.next=curr
                curr.next=None
                tail=tail.next
            else:
                break
            l+=2
            prev=prev.next
            curr=prev.next
        return head