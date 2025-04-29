class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans=""
        balance=0
        res=[]
        for i in s:
            if i=='(':
                if balance>0:
                    ans+='('
                balance+=1
            else:
                balance-=1
                if balance>0:
                    ans+=')'
            
        return ans
        
                    

            

        