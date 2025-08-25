class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums1=sorted(nums)
        for i in range(len(nums)-1):
            if nums1[i]==nums1[i+1]:
                return True
        return False