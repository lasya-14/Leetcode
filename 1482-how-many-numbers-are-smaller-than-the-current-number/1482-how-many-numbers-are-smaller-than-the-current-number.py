class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        li=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[i]>nums[j]:
                    count+=1
            li.append(count)
        return li
            
        