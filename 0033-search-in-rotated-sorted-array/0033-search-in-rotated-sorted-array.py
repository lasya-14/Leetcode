class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sor=[]
        sor.extend(nums)
        sor.sort()
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if target>sor[mid]:
                low=mid+1
            elif target<sor[mid]:
                high=mid-1
            elif target==sor[mid]:
                return nums.index(target)
        return -1
        