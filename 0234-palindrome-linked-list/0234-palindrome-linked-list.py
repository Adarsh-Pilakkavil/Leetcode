# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ptr=head
        l=[]
        while ptr!=None:
            l.append(ptr.val)
            ptr=ptr.next
        k=len(l)-1
        s=0
        while s<k:
            if l[s]!=l[k]:
                return False
            s+=1
            k-=1
        return True