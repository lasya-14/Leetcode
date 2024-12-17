class Solution:
    def climbStairs(self, n: int) -> int:
        pre=0
        post=1
        p=pre+post
        for i in range(n):
            p=pre+post
            pre=post
            post=p
        return p