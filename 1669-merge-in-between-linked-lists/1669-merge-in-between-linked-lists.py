# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start=list1
        finish=list1
        for i in range(a-1):
            start=start.next
        for i in range(b+1):
            finish=finish.next
        start.next=list2
        curr=list2
        while curr.next!=None:
            curr=curr.next
        curr.next=finish
        return list1