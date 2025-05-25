class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum=0
        sums=sum(nums)
        for idx,ele in enumerate(nums):
            sums-=ele
            if leftsum==sums:
                return idx
            leftsum+=ele
        return -1

        
        