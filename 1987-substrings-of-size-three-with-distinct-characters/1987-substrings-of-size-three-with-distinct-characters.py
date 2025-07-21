class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        count=0
        k=3
        dici={}
        l=0
        for r in range(n):
            if s[r] in dici:
                dici[s[r]]+=1
            else:
                dici[s[r]]=1
            if r-l==k:
                dici[s[l]]-=1
                if dici[s[l]]==0:
                    dici.pop(s[l])
                l+=1
            if len(dici)==k:
                count+=1
        return count