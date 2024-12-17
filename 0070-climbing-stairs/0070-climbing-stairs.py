class Solution:
    def climbStairs(self, n: int) -> int:
        p=[1]*(n+1)
        for i in range(2,n+1):
            p[i]=p[i-1]+p[i-2]
        return p[n]