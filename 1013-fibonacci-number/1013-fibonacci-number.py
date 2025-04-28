class Solution:
    def fib(self, n: int) -> int:
        pre=0
        post=1
        ans=0
        if n==0:
            return 0
        elif n==1:
            return 1
        for i in range(1,n):
            ans=pre+post
            pre=post
            post=ans
        return ans
        