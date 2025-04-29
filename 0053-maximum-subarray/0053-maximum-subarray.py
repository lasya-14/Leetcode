class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=nums[0]
        total=0
        if len(nums)==1:
            return nums[-1]
        for i in range(len(nums)):
            if total<0:
                total=0
            total+=nums[i]
            res=max(res,total)
        return res
        

        