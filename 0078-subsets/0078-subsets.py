class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        subsets=(1<<n)
        for i in range(subsets):
            li=[]
            for j in range(n):
                if (i&(1<<j))!=0:
                    li.append(nums[j])
            ans.append(li)
        return ans