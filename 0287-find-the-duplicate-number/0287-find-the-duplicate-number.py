class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d=collections.Counter(nums)
        for i,j in d.items():
            if j>1:
                return i
       