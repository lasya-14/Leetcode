class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dici={}
        for i in nums:
            if i not in dici:
                dici[i]=1
            else:
                dici[i]+=1
        n=len(nums)
        for i in dici:
            if dici[i]>(n//2):
                return i


