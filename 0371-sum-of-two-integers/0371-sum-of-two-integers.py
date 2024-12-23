class Solution:
    def getSum(self, a: int, b: int) -> int:
        m=0xffffffff
        while (b&m)!=0:
            c=(a&b)<<1
            a^=b
            b=c
        return a if b==0 else a&m