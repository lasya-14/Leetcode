# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        p=head
        r=''
        while p!=None:
            r+=str(p.val)
            p=p.next
        return int(r,2)
        