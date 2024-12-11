# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p=l1
        q=l2
        s=t=''
        while p!=None:
            s+=str(p.val)
            p=p.next
        while q!=None:
            t+=str(q.val)
            q=q.next
        ans=str(int(s[::-1])+int(t[::-1]))[::-1]
        p=l1
        while p.next!=None:
            p=p.next
        p.next=l2
        p=l1
        for i in range(len(ans)):
            p.val=int(ans[i])
            if i!=len(ans)-1:
                p=p.next
            else:
                p.next=None
        return l1
        