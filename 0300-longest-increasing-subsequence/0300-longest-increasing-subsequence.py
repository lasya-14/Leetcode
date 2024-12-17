class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        t=[1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    t[i]=max(t[i],1+t[j])
        return max(t)