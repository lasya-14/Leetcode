class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        t=[[False]*(len(p)+1) for i in range(len(s)+1)]
        t[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                t[0][i]=t[0][i-1]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    t[i][j]=t[i-1][j-1]
                elif p[j-1]=='*':
                    t[i][j]=t[i-1][j] or t[i][j-1]
        return t[-1][-1]

        