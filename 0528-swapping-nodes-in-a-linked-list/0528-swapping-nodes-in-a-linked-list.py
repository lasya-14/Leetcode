# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p=head
        r=[]
        while p!=None:
            r.append(p.val)
            p=p.next
        temp=r[k-1]
        r[k-1]=r[len(r)-k]
        r[len(r)-k]=temp
        p=head
        for i in r:
            p.val=i
            p=p.next
        return head
            
        