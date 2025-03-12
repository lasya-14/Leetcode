class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pcount,ncount=0,0
        for i in nums:
            if i>0:
                pcount+=1
            elif i<0:
                ncount+=1
        return max(pcount,ncount)
        