class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums)
        left=0
        for i in range(len(nums)):
            right_total=total-left-nums[i]
            if right_total==left:
                return i
            left+=nums[i]
        return -1
        

        
        