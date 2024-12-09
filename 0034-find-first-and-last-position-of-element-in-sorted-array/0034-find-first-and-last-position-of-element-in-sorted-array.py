class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        li=[]
        if target in nums:
            li.append(nums.index(target))
            li.append(len(nums)-1-nums[::-1].index(target))
        else:
            li.extend([-1,-1])
        return li
