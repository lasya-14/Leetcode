class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        h=len(nums)-1
        while l<=h:
            mid=(l+h)//2
            if nums[mid]==nums[l]:
                break
            elif nums[mid]-nums[l]<(mid-l):
                h=mid
            elif nums[mid]-nums[l]>=(mid-l):
                l=mid
        return nums[mid]