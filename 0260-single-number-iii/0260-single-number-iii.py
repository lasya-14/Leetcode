class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        li=[]
        for i in nums:
            if nums.count(i)==1:
                li.append(i)
        return li
        