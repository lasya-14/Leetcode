class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        t=n
        d=0
        while t>1:
            if t%4==0:
                d+=1
            t=t//4
        f=1
        for i in range(d):
            f*=4
        return f==n
        