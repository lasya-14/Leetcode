class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res=[]
        def dfs(num,n,k):
            if n==0:
                res.append(num)
                return
            rem=num%10
            if  rem+k<=9:
                dfs(num*10+rem+k,n-1,k)
            if k>0 and rem-k>=0:
                dfs(num*10+rem-k,n-1,k)
        for i in range(1,10):
            dfs(i,n-1,k)
        return res
        