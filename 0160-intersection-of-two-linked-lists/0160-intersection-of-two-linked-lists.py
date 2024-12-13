# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p=headA
        q=headB
        while p!=q:
            if p:
                p=p.next
            else:
                p=headB
            if q:
                q=q.next
            else:
                q=headA
        if p==q:
            return p


        