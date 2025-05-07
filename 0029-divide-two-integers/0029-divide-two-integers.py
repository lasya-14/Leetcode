class Solution:
    def divide(self, n: int, p: int) -> int:
        if n==p:
            return 1
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        sign=True
        if n>0 and p<0:
            sign=False
        if n<0 and p>0:
            sign=False
        n=abs(n)
        p=abs(p)
        ans=0
        while n>=p:
            count=0
            while n>=(p<<(count+1)):
                count+=1
            ans+=(1<<count)
            n=n-(p*(1<<count))
        if ans>2**31 and sign==True:
            return INT_MAX
        if ans>2**31 and sign==False:
            return INT_MIN
        if sign:
            return min(max(INT_MIN, ans), INT_MAX)
        else:
            return -ans


        