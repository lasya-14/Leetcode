class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,h=0,len(nums)-1
        while l<h:
            mid=(l+h)//2
            if nums[mid-1]<=nums[mid] and nums[mid]>nums[mid+1]:
                return mid
            if nums[mid]<nums[mid+1]:
                l=mid+1
            else:
                h=mid-1
        return l
        