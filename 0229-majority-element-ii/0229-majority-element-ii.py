class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            if nums.count(nums[i])>len(nums)//3:
                if nums[i] not in res:
                    res.append(nums[i])
        return res
        