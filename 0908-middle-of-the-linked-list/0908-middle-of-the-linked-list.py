# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        count=0
        while temp:
            count+=1
            temp=temp.next
        if count==1:
            return head
        count1=0
        dummy=head
        while dummy:
            count1+=1
            if count1==(count//2):
                return dummy.next
            dummy=dummy.next
        
        
        