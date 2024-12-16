class Solution:
    def checkValidString(self, s: str) -> bool:
        l,r=0,0
        for i in s:
            if i=='(':
                l+=1
                r+=1
            elif i==')':
                l-=1
                r-=1
            else:
                l-=1
                r+=1
            if r<0:
                return False
            l=max(l,0)
        return l==0
        