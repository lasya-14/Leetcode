class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inc=[0]*(n+1)
        out=[0]*(n+1)
        for i,j in trust:
            inc[j]+=1
            out[i]+=1
        for i in range(1,n+1):
            if inc[i]==n-1 and out[i]==0:
                return i
        return -1
        