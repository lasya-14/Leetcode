class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        count=0
        for i in range(n):
            for j in range(i,n):
                temp=[]
                for k in range(i,j+1):
                    temp.append(s[k])
                if len(temp)==3 and len(set(temp))==3:
                    count+=1
        return count