# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        li=[]
        while head:
            li.append(head.val)
            head=head.next
        low=0
        high=len(li)-1
        while low<high and li[low]==li[high]:
            low+=1
            high-=1
        return low>=high
        