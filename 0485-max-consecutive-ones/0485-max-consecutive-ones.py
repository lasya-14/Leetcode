class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        res=[]
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            elif nums[i]==0:
                res.append(count)
                count=0
        res.append(count)
        return max(res)
        