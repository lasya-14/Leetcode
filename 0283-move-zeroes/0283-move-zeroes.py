class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        res=[]
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
            else:
                res.append(nums[i])
        for i in range(count):
            res.append(0)
        nums[:]=res
        