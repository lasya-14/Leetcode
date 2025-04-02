class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    res1=(nums[i] - nums[j]) * nums[k]
                    if res1>res:
                        res=(nums[i] - nums[j]) * nums[k]
                    
        return res
