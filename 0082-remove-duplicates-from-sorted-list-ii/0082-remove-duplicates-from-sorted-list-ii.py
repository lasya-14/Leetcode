class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        lis=[]
        while p!=None:
            lis.append(p.val)
            p=p.next
        d=collections.Counter(lis)
        lis=[]
        for i,h in d.items():
            if h==1:
                lis.append(i)
        if len(lis)==0:
            return None
        p=head
        for i in range(len(lis)):
            p.val=lis[i]
            if i!=len(lis)-1:
                p=p.next
            else:
                p.next=None
        return head
            


        
        
        