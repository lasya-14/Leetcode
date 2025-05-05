class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sor=[]
        sor.extend(nums)
        sor.sort()
        low=0
        high=len(sor)-1
        while low<=high:
            mid=(low+high)//2
            if sor[mid]==target:
                return nums.index(target)
            elif sor[mid]>target:
                high=mid-1
            elif sor[mid]<target:
                low=mid+1
        return -1
