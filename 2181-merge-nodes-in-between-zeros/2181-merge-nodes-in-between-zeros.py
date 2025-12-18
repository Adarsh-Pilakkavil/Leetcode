# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head.next
        a=ListNode(-1)
        curr2=a
        su=0
        l=[]
        while curr!=None:
            if curr.val==0:
                b=ListNode(su)
                curr2.next=b
                su=0
                curr2=curr2.next
            else:
                su+=curr.val
            curr=curr.next
        return a.next