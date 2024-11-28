class Solution:
    def defangIPaddr(self, address: str) -> str:
        res=''
        for i in address:
            if i!='.':
                res+=i
            elif i=='.':
                v=i.replace('.','[.]')
                res+=v
        return res


        