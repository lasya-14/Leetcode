class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        t=[amount+1]*(amount+1)
        t[0]=0
        for i in range(1,amount+1):
            for j in coins:
                if i-j>=0:
                    t[i]=min(t[i],1+t[i-j])
        return t[-1] if t[-1]!=amount+1 else -1
        