# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st=[]
        temp=head
        while temp:
            st.append(temp.val)
            temp=temp.next
        temp=head
        while temp:
            value=st.pop(-1)
            temp.val=value
            temp=temp.next
           
        return head


        
