class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d=Counter(nums)
        for i,j in d.items():
            if j>=2:
                return True
        return False
