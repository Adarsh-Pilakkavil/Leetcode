# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=[]
        s2=[]
        curr=l1
        while curr!=None:
            s1.append(curr.val)
            curr=curr.next
        curr=l2
        while curr!=None:
            s2.append(curr.val)
            curr=curr.next
        curr=ListNode(0)
        a=curr
        c=0
        while s1!=[] or s2!=[]:
            total=c
            c=0
            if s1==[]:
                total+=s2.pop()
                if total>=10:
                    c=1
                    total-=10
                a.next=ListNode(total)
                a=a.next
                continue
            if s2==[]:
                total+=s1.pop()
                if total>=10:
                    c=1
                    total-=10
                a.next=ListNode(total)
                a=a.next
                continue
            total+=s1.pop()+s2.pop()
            if total>=10:
                c=1
                total-=10
            a.next=ListNode(total)
            a=a.next
        if c==1:
            a.next=ListNode(1)
        curr=curr.next
        prev=None
        while curr!=None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev

                