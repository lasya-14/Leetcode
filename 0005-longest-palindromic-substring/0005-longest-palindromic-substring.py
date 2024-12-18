class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=[[0]*len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i]=1
        maxlength=1
        start=0
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=1
                maxlength=2
                start=i
        for length in range(3,len(s)+1):
            for i in range(len(s)-length+1):
                j=i+length-1
                if s[i]==s[j] and dp[i+1][j-1]==1:
                    dp[i][j]=1
                    maxlength=length
                    start=i

        return s[start:start+maxlength]
        