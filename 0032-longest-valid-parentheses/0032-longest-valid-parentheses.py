class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l,r,tot=0,0,0
        for i in s:
            if i=='(':
                l+=1
            elif i==')':
                r+=1
            if r>l:
                l=r=0
            elif r==l:
                tot=max(tot,l*2)
        l,r=0,0
        for i in s[::-1]:
            if i=='(':
                l+=1
            elif i==')':
                r+=1
            if l>r:
                l=r=0
            elif r==l:
                tot=max(tot,l*2)
        return tot


        