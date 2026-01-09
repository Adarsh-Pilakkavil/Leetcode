# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import fractions
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next:
            return head
        prev=head
        curr=head.next
        while curr!=None:
            prev.next=ListNode(fractions.gcd(prev.val,curr.val))
            prev.next.next=curr
            prev=curr
            curr=curr.next
        return head 