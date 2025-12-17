# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=0
        curr=head
        while curr!=None:
            curr=curr.next
            l+=1
        curr=head
        if l==0 or l==1:
            return head
        if k>l:
            if k==l:
                return head
            else:
                k=k%l
        
        while k!=0:
            curr=head
            last=head
            for i in range(l-2):
                last=last.next
            last.next.next=head
            head=last.next
            last.next=None
            k-=1
        return head