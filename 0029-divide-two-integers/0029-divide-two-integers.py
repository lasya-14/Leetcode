class Solution:
    def divide(self, n: int, p: int) -> int:
        r=1
        t=p
        if n==-(2**31) and p==-1:
            return (n*-1)-1
        if n<0:
            n=-n
            r=-1
        if p<0:
            p=-p
            r*=-1
        def divided(n,p,r):
            d=0
            while p<=n:
                w=1
                t=p
                while t<<1<=n:
                    w<<=1
                    t<<=1
                d+=w
                n-=t
            return r*d
        s=divided(n,p,r)
        return s
        