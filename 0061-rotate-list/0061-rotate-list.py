# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        l=1
        curr=head
        while curr.next!=None:
            curr=curr.next
            l+=1
        curr.next=head
        k=k%l
        st=l-k
        lt=head
        for i in range(st-1):
            lt=lt.next
        hea=lt.next
        lt.next=None
        return hea