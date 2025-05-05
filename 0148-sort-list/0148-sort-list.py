# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        li=[]
        temp=head
        while temp:
            li.append(temp.val)
            temp=temp.next
        li.sort()
        temp=head
        i=0
        while temp:
            temp.val=li[i]
            temp=temp.next
            i+=1
        return head