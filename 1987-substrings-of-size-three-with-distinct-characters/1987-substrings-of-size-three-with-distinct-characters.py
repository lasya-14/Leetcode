class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        temp=''
        res=[]
        k=3
        l=0
        for r in range(len(s)):
            temp+=s[r]
            if(r-l+1>k):
                temp=temp[1:]
                l+=1
            if(r-l+1==k):
                res.append(temp)
        count=0
        for i in range(len(res)):
            if len(set(res[i]))==k:
                count+=1
        return count


        