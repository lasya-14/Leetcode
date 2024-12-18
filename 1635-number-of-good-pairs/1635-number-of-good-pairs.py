class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dici={}
        for i in nums:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        ans=0
        for i in dici:
            n=dici[i]
            ans+=n*(n-1)//2
        return ans
        