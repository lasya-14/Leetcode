class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def back(start):
            if start==len(nums):
                res.append(nums[:])
            for i in range(start,len(nums)):
                nums[i],nums[start]=nums[start],nums[i]
                back(start+1)
                nums[i],nums[start]=nums[start],nums[i]
        back(0)
        return res

        