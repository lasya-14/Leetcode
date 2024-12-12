class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minVal = nums[0]
        maxDiff = -1
        for num in nums:
            if num > minVal:
                diff = num - minVal
                maxDiff = max(maxDiff, diff)
            else:
                minVal = num
        return maxDiff
        