class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        d=Counter(nums)
        for i,j in d.items():
            if j==1:
                return i
        