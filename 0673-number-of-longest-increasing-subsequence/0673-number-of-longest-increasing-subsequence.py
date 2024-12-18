class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        l=[1]*(n)
        c=[1]*(n)
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if l[i]<1+l[j]:
                        l[i]=l[j]+1
                        c[i]=c[j]
                    elif l[i]==1+l[j]:
                        c[i]+=c[j]
        mx=max(l)
        tot=0
        for i,j in zip(l,c):
            if i==mx:
                tot+=j
        return tot

        