# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p=[]
        t=s=f=head
        for i in range(1,n):
            f=f.next
        if s.next==None:
            head=None
        while f.next!=None:
            t=s
            f=f.next
            s=s.next
        if s==head:
            return head.next
        t.next=s.next
        return head

        