class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def back(nums,res,temp,start):
            res.append(temp[:])
            for i in range(start,len(nums)):
                if i > start and nums[i]==nums[i-1]:
                    continue
                temp.append(nums[i])
                back(nums,res,temp,i+1)
                temp.pop()
        back(nums,res,[],0)
        return res