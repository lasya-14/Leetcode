class Solution:
    def findMin(self, nums: List[int]) -> int:
        mine=nums[0]
        for i in range(len(nums)):
            if nums[i]<mine:
                mine=nums[i]
        return mine
        