class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        dici={}
        for i in nums:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        ans=-1
        for i in dici:
            val=dici[i]
            if dici[i]>n//2:
                ans=i
                break
        return ans
        