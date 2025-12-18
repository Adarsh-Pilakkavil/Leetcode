# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr=head
        l=0
        while curr!=None:
            l+=1
            curr=curr.next
        l-=1
        curr=head
        d=0
        while curr!=None:
            d+=(2**l)*(curr.val)
            curr=curr.next
            l-=1
        return d