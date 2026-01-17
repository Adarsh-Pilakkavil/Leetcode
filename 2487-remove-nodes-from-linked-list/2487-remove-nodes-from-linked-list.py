# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        curr2=dummy
        curr=head
        stack=[]
        while curr!=None:
            if stack and curr.val>stack[-1]:
                stack.pop()
                continue
            stack.append(curr.val)
            curr=curr.next
        curr=head
        while stack and curr!=None:
            if curr.val==stack[0]:
                stack.pop(0)
                curr2.next=ListNode(curr.val)
                curr2=curr2.next
            curr=curr.next
        return dummy.next