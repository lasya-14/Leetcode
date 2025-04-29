class Solution:
    def check(self, nums: List[int]) -> bool:
        s=sorted(nums)
        if nums==s:
            return True
        ind=0
        for i in range(len(nums)):
            if nums[i]<nums[i-1]:
                ind=i
                break
        nums[i:],nums[:i]=nums[:i],nums[i:]
        for i in range(len(nums)):
            if nums[i]!=s[i]:
                return False
        return True
        
        