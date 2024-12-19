class Solution:
    def calculateMinimumHP(self, g: List[List[int]]) -> int:
        dp=[[0]*len(g[0]) for i in range(len(g))]
        dp[-1][-1]=1 if g[-1][-1]>0 else (1-g[-1][-1])
        r=len(g)
        c=len(g[0])
        for i in range(r-2,-1,-1):
            dp[i][c-1]=max(1,dp[i+1][c-1]-g[i][c-1])
        for i in range(c-2,-1,-1):
            dp[r-1][i]=max(1,dp[r-1][i+1]-g[r-1][i])
        for i in range(r-2,-1,-1):
            for j in range(c-2,-1,-1):
                dp[i][j]=max(min(dp[i][j+1],dp[i+1][j])-g[i][j],1)
        return dp[0][0]

        