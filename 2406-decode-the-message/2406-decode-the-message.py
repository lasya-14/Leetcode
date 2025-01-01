class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dici={}
        ans=''
        temp=97
        for i in key:
            if i not in dici and i!=' ':
                dici[i]=chr(temp)
                temp+=1
        for i in message:
            if i==' ':
                ans+=' '
            else:
                ans+=dici[i]
        return ans

        