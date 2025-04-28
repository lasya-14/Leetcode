class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=set(nums)
        if len(s)<=2:
            return max(nums)
        arr=list(s)
        arr.sort(reverse=True)
        return arr[2]
        