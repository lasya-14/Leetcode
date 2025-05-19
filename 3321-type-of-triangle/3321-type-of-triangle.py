class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0]+nums[1]>nums[2] and nums[1]+nums[2]>nums[0] and nums[2]+nums[0]>nums[1]:
            for i in range(len(nums)):
                if nums[i]==nums[i+1] and nums[i+1]==nums[i+2] and nums[i]==nums[i+2]:
                    return "equilateral"
                elif nums[i]==nums[i+1] or nums[i+1]==nums[i+2] or nums[i]==nums[i+2]:
                    return "isosceles"
                else:
                    return "scalene"
        else:
            return "none"
        